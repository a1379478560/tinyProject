import requests
from bs4 import BeautifulSoup
import os
import xlwt
def getOnePageData(city,kw,page,):
    position=[]
    headers = {
        'Host': 'sou.zhaopin.com',
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.104 Safari/537.36 Core/1.53.4620.400 QQBrowser/9.7.13014.400',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Accept-Language': 'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3',
        'Accept-Encoding': 'gzip, deflate, sdch, br',
        'Connection': 'keep-alive',
        'Cache-Control': 'max-age=0',
        'Upgrade-Insecure-Requests':'1',
    }

    zhilianUrl = "http://sou.zhaopin.com/jobs/searchresult.ashx"

    params={
        'jl':city,
        'kw':kw,
        'p':page,
        'isadv':'0',
    }
    r=requests.get(zhilianUrl,headers=headers,params=params)
    soup=BeautifulSoup(r.text,'html.parser')
    pos_num=soup.find('em').text
    trs=soup.find_all('tr',{'class':False})
    trs=trs[1:]
    for tr in trs:
        pos_name=tr.find_all('a')[0].text.replace('\xa0','')
        com_name=tr.find('td',{'class':'gsmc'}).find('a').text
        salary=tr.find('td',{'class':'zwyx'}).text
        site=tr.find('td',{'class':'gzdd'}).text
        fankuilv=tr.find('td',{'class':'fk_lv'}).text
        updatetime=tr.find('td',{'class':'gxsj'}).find('span').text
        item=(pos_name,com_name,salary,site,fankuilv,updatetime)
        position.append(item)
    return position,pos_num

def getAllData(city,kw,pages,start_page=1):
    POSITION=[]
    I=0
    print('开始爬取数据')
    for i in range(start_page,pages+1):
        print('开始第%s页...'%(i))
        position,pos_num=getOnePageData(city,kw,i)
        POSITION+=position
        print('ok')
        if i >=int(pos_num)//60+1:
            I=i
            break
    return POSITION,I  #i是实际爬取的页数，因为输入的页数可能大于实际有的页数

def save_xls(path,filename,data):
    filename+='.xls'
    print('保存文件到%s'% os.path.join(path,filename))
    wbk = xlwt.Workbook(encoding='ascii')
    sheet1 = wbk.add_sheet('智联招聘数据')
    sheet1.write(0,0,'职位名称')
    sheet1.write(0, 1, '公司名称')
    sheet1.write(0, 2, '月薪')
    sheet1.write(0, 3, '上班地点')
    sheet1.write(0, 4, '反馈率')
    sheet1.write(0, 5, '更新时间')
    raw=1
    for x in data:
        sheet1.write(raw, 0, x[0])
        sheet1.write(raw, 1, x[1])
        sheet1.write(raw, 2, x[2])
        sheet1.write(raw, 3, x[3])
        sheet1.write(raw, 4, x[4])
        sheet1.write(raw, 5, x[5])
        raw+=1
    wbk.save( os.path.join(path,filename))

if __name__=="__main__":
    flag=1
    kw=input('请输入要爬取的关键字,直接回车默认会计\n')
    if kw=='':
        kw='会计'
    city=input('请输入要爬取得城市，默认北京\n')
    if city=='':
        city='北京'

    while(flag):
        page_num=input('请输入要爬取得页数，默认5页\n')
        if page_num=='':
            page_num=5
            flag=0
        else:
            try:
                page_num=int(page_num)
                flag=0
            except:
                print('请输入整数')

    scores, I=getAllData(city, kw, page_num)
    num=len(scores)
    print('全部爬取完成，共爬取%s条数据，正在存入Excel'%(num))
    save_xls('', city +'-' + kw, scores)
    print('保存成功！已保存在程序目录下并命名为城市+关键词.xls')

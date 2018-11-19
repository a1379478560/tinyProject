import requests
import xlwt
from bs4 import BeautifulSoup

def get_data(win_odds,draw_odds,lose_odds,return_asian_handicap,return_goal_line,return_score):
    data={}
    url='http://www.jq007.com/page/ouyazhuanhuan/%E6%AC%A7%E4%BA%9A%E8%BD%AC%E6%8D%A2'
    header = {
        'User-Agent': r'Agent:Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.104 Safari/537.36 Core/1.53.4843.400 QQBrowser/9.7.13021.400',
    }
    params={
        'win_odds':win_odds,
        'draw_odds':draw_odds,
        'lose_odds':lose_odds,
        'return_asian_handicap':return_asian_handicap,
        'return_goal_line':return_goal_line,
        'return_score':return_score,
    }
    r=requests.post(url=url,headers=header,data=params)
    soup=BeautifulSoup(r.text,'html.parser')
    row=soup.find_all('div',{'class':'row'})[1:3]
    span=row[0].find_all('span',{'class':'spantext'})
    data['gailv']=(span[0].text,span[1].text,span[2].text,span[3].text,)
    div=row[1].find_all('div',{'class':'col-sm-4'})
    yapan=div[0].find('table').find_all('tr')[1:]
    daxiaoqiu=div[1].find('table').find_all('tr')[1:]
    bifen=div[2].find('table').find_all('tr')

    data['yapan']=map(lambda x:(x.find_all('td')[0].text,x.find_all('td')[1].text,x.find_all('td')[2].text),yapan)
    data['daxiaoqiu']=map(lambda x:(x.find_all('td')[0].text,x.find_all('td')[1].text,x.find_all('td')[2].text),daxiaoqiu)
    data['yapan'] = list(data['yapan'])
    data['daxiaoqiu'] = list(data['daxiaoqiu'])
    temp=[]
    for tr in bifen:
        tds=tr.find_all('td')
        tmp=[]
        for td in tds:
            span=td.find_all('span')
            if len(span)<2:
                score_str=""
                score_float="0"
            else:
                score_str=span[0].text
                score_float=span[1].text
            tmp.append(((score_str,score_float)))
        temp.append(tmp)
    data['bifen']=temp
    return data


def writexls(data,fileName):
    wbk=xlwt.Workbook(encoding='ascii')
    sheet1=wbk.add_sheet("亚盘")
    sheet2=wbk.add_sheet("大小球")
    sheet3=wbk.add_sheet("比分")
    sheet4=wbk.add_sheet("胜平负概率")

    sheet1.write(0,0,"盘口")
    sheet1.write(0,1,"主队")
    sheet1.write(0,2,"客队")
    row=1
    yapan=data['yapan']
    for x in yapan:
        sheet1.write(row,0,float(x[0].replace(",",'')))
        sheet1.write(row,1,float(x[1].replace(",",'')))
        sheet1.write(row,2,float(x[2].replace(",",'')))
        row+=1

    sheet2.write(0,0,'盘口')
    sheet2.write(0,1,"大球")
    sheet2.write(0,2,'小球')
    daxiaoqiu=data['daxiaoqiu']
    row=1
    for x in daxiaoqiu:
        sheet2.write(row,0,float(x[0].replace(",",'')))
        sheet2.write(row,1,float(x[1].replace(",",'')))
        sheet2.write(row,2,float(x[2].replace(",",'')))
        row+=1

    bifen=data['bifen']
    row=0
    for x in bifen:
        sheet3.write(row,0,x[0][0])
        sheet3.write(row,1,float(x[0][1].replace(",",'')))
        if x[1][0]!='':
            sheet3.write(row,2,x[1][0])
            sheet3.write(row,3,float(x[1][1].replace(",",'')))
        sheet3.write(row,4,x[2][0])
        sheet3.write(row,5,float(x[2][1].replace(",",'')))
        row+=1

    gailv=data['gailv']
    row=1
    sheet4.write(0,0,'胜')
    sheet4.write(0,1,"平")
    sheet4.write(0,2,'负')
    sheet4.write(row,0,float(gailv[0][:-1])/100)
    sheet4.write(row,1,float(gailv[1][:-1])/100)
    sheet4.write(row,2,float(gailv[2][:-1])/100)
    sheet4.write(row, 3, gailv[3])

    wbk.save(fileName)


if __name__ == '__main__':
    zhusheng = input("请输入主胜赔率：")
    pingju = input("请输入平局赔率：")
    kesheng = input("请输入客胜赔率：")
    yafan = input("请输入返还率（亚盘）：")
    daxiaofan = input("请输入返还率（大小球）：")
    bifenfan = input("请输入返还率（比分）：")
    d=list(map(lambda x: float(x),[zhusheng,pingju,kesheng,yafan,daxiaofan,bifenfan,]))
    fileName=input('请输入要保存的文件名（默认角球之家）：')
    if fileName=="":
        fileName='角球之家'

    d=get_data(*d)
    writexls(d,fileName+".xls")
    print("爬取完成！")
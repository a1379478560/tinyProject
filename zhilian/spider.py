import requests
from bs4 import BeautifulSoup
from zhilian.zhilian_com import STATUS,POSITION,addlog,I
def getonepagedata(city,kw,page,):
    position=[]
    headers = {
        'Host': 'sou.zhaopin.com',
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.104 Safari/537.36 Core/1.53.4620.400 QQBrowser/9.7.13014.400',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Accept-Language': 'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3',
        'Accept-Encoding': 'gzip, deflate, sdch, br',
        #'Referer': 'http://www.zhaopin.com',
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
    pos_num=soup.find('em')
    trs=soup.find_all('tr',{'class':False})
    #lis=list(map(lambda x:x.find('li'),trs))
    trs=trs[1:]
    for tr in trs:
        #print(tr)
        pos_name=tr.find_all('a')[0].text.replace('\xa0','')
        com_name=tr.find('td',{'class':'gsmc'}).find('a').text
        salary=tr.find('td',{'class':'zwyx'}).text
        site=tr.find('td',{'class':'gzdd'}).text
        fankuilv=tr.find('td',{'class':'fk_lv'}).text
        updatetime=tr.find('td',{'class':'gxsj'}).find('span').text
        item=(pos_name,com_name,salary,site,fankuilv,updatetime)
        position.append(item)
    return position,pos_num.text



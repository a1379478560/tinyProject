import requests
import  xlwt
from  bs4 import BeautifulSoup
import os
import re

def getallid():
    all_id=[]
    headers={
        'Host':r'a.haocai138.com',
        'User-Agent': r'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.104 Safari/537.36 Core/1.53.4843.400 QQBrowser/9.7.13021.400',
    }
    origin_url=r'http://a.haocai138.com/info/match/Zucai.aspx'
    r=requests.get(origin_url,headers=headers)
    soup=BeautifulSoup(r.text,'html.parser')
    origin_id=soup.find('option').text
    origin_id=int(origin_id)
    print('今天的赛事编号是：',origin_id)
    id_url='http://a.haocai138.com/info/match/Zucai.aspx?typeID=1&issueNum='+str(origin_id)
    r=requests.get(id_url,headers=headers)
    soup=BeautifulSoup(r.text,'html.parser')
    trs=soup.find_all('tr',{'matchid':True})
    for tr in trs:
        a=tr.find_all('a')[1]
        all_id.append(a['href'])
    return  all_id
def f(xx):
    return xx['id']
def toint(x):
    if x=='':
        return 0
    x=x.replace(',','')
    return int(x)

def getxls(id,s,ii):

    headers={
        'Host':r'c.spdex.com',
        'User-Agent': r'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.104 Safari/537.36 Core/1.53.4843.400 QQBrowser/9.7.13021.400',
    }
    url=r'http://c.spdex.com/Match/View/Normal/'
    r=s.get(url+id,headers=headers)
    soup=BeautifulSoup(r.text,'html.parser')
    #print(soup.find('title'))
    try:
        n=soup.find('td',{'valign': 'bottom','nowrap': 'true',}).text[8:10]
    except:
        print('这个没有数据')
        return
    n=int(n)
    print(n,'页','ok')
    wbk = xlwt.Workbook(encoding='ascii')
    sheet1 = wbk.add_sheet('sheet1')
    sheet2 = wbk.add_sheet('sheet2')
    sheet3 = wbk.add_sheet('sheet3')
    sheet2.write(0, 0, '时间')
    sheet2.write(0, 1, '价位')
    sheet2.write(0, 2, '成交量')
    sheet2.write(0, 3, '成交变化')
    sheet2.write(0, 4, '属性')

    sheet3.write(0, 0, '时间')
    sheet3.write(0, 1, '价位')
    sheet3.write(0, 2, '成交量')
    sheet3.write(0, 3, '成交变化')
    sheet3.write(0, 4, '属性')

    sheet1.write(0, 0, '时间')
    sheet1.write(0, 1, '价位')
    sheet1.write(0, 2, '成交量')
    sheet1.write(0, 3, '成交变化')
    sheet1.write(0, 4, '属性')
    sheet1.write(0,5,'挂牌倾向')
    sheet3.write(0,5,'挂牌倾向')
    sheet2.write(0,5,'挂牌倾向')
    row=1
    for i in range(1,n+1):
        r=s.get(url+id+'/?page='+str(i))
        soup=BeautifulSoup(r.text,'html.parser')
        tr=soup.find_all('tr',{'class': False})
        for x in tr:
            td=x.find_all('td')
            if len(td)==16 :
                time=td[0].text
                sheet1.write(row,0,time)
                sheet2.write(row, 0, time)
                sheet3.write(row, 0, time)
                sheet1.write(row,1,float(td[1].text))
                sheet2.write(row, 1, float(td[6].text))
                sheet3.write(row, 1, float(td[11].text))
                sheet1.write(row,2,toint(td[2].text))
                sheet2.write(row,2, toint(td[7].text))
                sheet3.write(row,2, toint(td[12].text))
                sheet1.write(row,3,toint(td[3].text))
                sheet2.write(row, 3, toint(td[8].text))
                sheet3.write(row,3, toint(td[13].text))
                sheet1.write(row,4,td[4].text)
                sheet2.write(row,4, td[9].text)
                sheet3.write(row,4, td[14].text)
                sheet1.write(row,5,td[5].text)
                sheet2.write(row, 5, td[10].text)
                sheet3.write(row, 5, td[15].text)
                row=row+1
    wbk.save(r'spdex_com/'+str(ii)+'.xls')
def getteamid(all_id):
    team=[]
    headers={
        'Host':r'a.haocai138.com',
        'User-Agent': r'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.104 Safari/537.36 Core/1.53.4843.400 QQBrowser/9.7.13021.400',
    }
    url='http://a.haocai138.com'
    pattern1 = re.compile(r'hometeamid=\d\d\d')
    pattern2 = re.compile(r'guestteamid=\d\d\d')
    for match in all_id:
        r=requests.get(url+match,headers=headers)
        team_id=pattern1.search(r.text)
        team_id=team_id.group()
        home_team_id=team_id[-3:]
        team_id=pattern2.search(r.text)
        team_id=team_id.group()
        guest_team_id=team_id[-3:]
        team.append((home_team_id,guest_team_id))
    return team
if __name__=='__main__':

    all_id=getallid()
    print('14场比赛id为：',all_id)
    teamid=getteamid(all_id)
    print(teamid)
    # if not os.path.exists('haocai138_com'):
    #     os.mkdir('haocai138_com')
    #     print('创建spdex_文件夹')
    # ii = 1  # 后面做文件名
    # for a in range(len(all_id)):
    #     getxls(all_id[a],s,ii)
    #     ii=ii+1
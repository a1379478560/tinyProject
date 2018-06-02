import requests
import  xlwt
from  bs4 import BeautifulSoup
import os
import re
import time
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

def getxls(id):

    headers={
        'Host':r'info.haocai138.com',
        'User-Agent': r'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.104 Safari/537.36 Core/1.53.4843.400 QQBrowser/9.7.13021.400',
    }
    url=r'http://info.haocai138.com/cn/team/lineup/'
    r1=requests.get(url+id[0],headers=headers)
    soup1=BeautifulSoup(r1.text,'html.parser')
    #time.sleep(1)
    r2 = requests.get(url + id[1], headers=headers)
    soup2 = BeautifulSoup(r2.text, 'html.parser')
    try:
        t1=soup1.find('title').text.split(',')[0]
        t2 = soup2.find('title').text.split(',')[0]
    except:
        print('这个没有数据')
        return

    print(t1,'vs',t2)
    wbk = xlwt.Workbook(encoding='ascii')
    sheet1 = wbk.add_sheet(t1)
    sheet2 = wbk.add_sheet(t2)
    sheet2.write(0, 0, '号码')
    sheet2.write(0, 1, '姓名')
    sheet2.write(0, 2, '生日')
    sheet2.write(0, 3, '身高')
    sheet2.write(0, 4, '体重')
    sheet2.write(0, 5, '位置')
    sheet2.write(0, 6, '国籍')
    sheet2.write(0, 7, '预计身价')
    sheet2.write(0, 8, '合同截止')
    sheet2.write(0, 9, '首发次数/进球')
    sheet2.write(0,10, '替补次数/进球')
    sheet2.write(0, 11, '助攻')

    sheet1.write(0, 0, '号码')
    sheet1.write(0, 1, '姓名')
    sheet1.write(0, 2, '生日')
    sheet1.write(0, 3, '身高')
    sheet1.write(0, 4, '体重')
    sheet1.write(0, 5, '位置')
    sheet1.write(0, 6, '国籍')
    sheet1.write(0, 7, '预计身价')
    sheet1.write(0, 8, '合同截止')
    sheet1.write(0, 9, '首发次数/进球')
    sheet1.write(0,10, '替补次数/进球')
    sheet1.write(0, 11, '助攻')
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

                sheet1.write(row,1,float(td[1].text))
                sheet2.write(row, 1, float(td[6].text))

                sheet1.write(row,2,toint(td[2].text))
                sheet2.write(row,2, toint(td[7].text))

                sheet1.write(row,3,toint(td[3].text))
                sheet2.write(row, 3, toint(td[8].text))

                sheet1.write(row,4,td[4].text)
                sheet2.write(row,4, td[9].text)

                sheet1.write(row,5,td[5].text)
                sheet2.write(row, 5, td[10].text)

                row=row+1
    wbk.save(r'haocai138_com/'+t1+'VS'+t2+'.xls')
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
    if not os.path.exists('haocai138_com'):
        os.mkdir('haocai138_com')
        print('创建spdex_文件夹')

    for a in teamid:
        getxls(a)

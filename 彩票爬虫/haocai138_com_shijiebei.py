import requests
import  xlwt
from  bs4 import BeautifulSoup
import os
import re
import datetime,time
def getallid():
    all_id=[]
    headers={
        'Host':r'a.haocai138.com',
        'User-Agent': r'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.104 Safari/537.36 Core/1.53.4843.400 QQBrowser/9.7.13021.400',
    }
    origin_url=r'http://a.haocai138.com/buy/toto14.aspx'
    r=requests.get(origin_url,headers=headers)
    soup=BeautifulSoup(r.text,'html.parser')
    origin_id=soup.find('a',{'class':'SelectedIssue'}).string[3:10]
    origin_id=int(origin_id)
    print('今天的赛事编号是：',origin_id)
    id_url='http://a.haocai138.com/buy/toto14.aspx'
    r=requests.get(id_url,headers=headers)
    pattern=re.compile(r'/Handle/Panlu.aspx\?id=\d{7}')
    all_id=pattern.findall(r.text)
    print(all_id)
    all_id=list(set(all_id))
    return  all_id
def f(xx):
    return xx['id']
def toint(x):
    if x=='':
        return 0
    x=x.replace(',','')
    return int(x)

def get2team(id):
    now_time = datetime.datetime.now().strftime('%Y%m%d')
    headers={
        'Host':r'info.haocai138.com',
        'User-Agent': r'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.104 Safari/537.36 Core/1.53.4843.400 QQBrowser/9.7.13021.400',
    }
    url=r'http://info.haocai138.com/cn/team/lineup/'
    url_js1='http://info.haocai138.com/jsData/teamInfo/teamDetail/tdl'+id[0]+'.js?version='+now_time
    url_js2 = 'http://info.haocai138.com/jsData/teamInfo/teamDetail/tdl' + id[1] + '.js?version=' + now_time
    r1=requests.get(url+id[0]+'.html',headers=headers)
    soup1=BeautifulSoup(r1.text,'html.parser')
    #time.sleep(1)
    r2 = requests.get(url + id[1]+'.html', headers=headers)
    soup2 = BeautifulSoup(r2.text, 'html.parser')
    print(r1.url)
    try:
        t1=soup1.find('title').text.split(',')[0]
        t2 = soup2.find('title').text.split(',')[0]
        t1=t1.replace(' ','')
        t2=t2.replace(' ','')
    except:
        print('这个没有数据')
        return

    print(t1,'vs',t2)

    r1=requests.get(url_js1,headers=headers)
    # pattern=re.compile(r'lineupDetail=*;')
    # lineup1=re.search(pattern,r1.text)
    #print(r1.text)
    lineup1=r1.text.split('lineupDetail=')[-1].split(';')[0]
    time.sleep(2)
    r2=requests.get(url_js2,headers=headers)
    lineup2=r2.text.split('lineupDetail=')[-1].split(';')[0]
    time.sleep(2)
    lineup1=eval(lineup1)
    lineup2=eval(lineup2)
    return (t1,t2),lineup1,lineup2
def getxls(two_team,lineup1,lineup2):
    t1=two_team[0]
    t2=two_team[1]
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
    sheet2.write(0,11,'助攻')

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
    for i in lineup1:
        sheet1.write(row, 0, i[1])
        sheet1.write(row, 1, i[2])
        sheet1.write(row, 2, i[5])
        sheet1.write(row, 3, i[6])
        sheet1.write(row, 4, i[7])
        sheet1.write(row, 5, i[8])
        sheet1.write(row, 6, i[9])
        sheet1.write(row, 7, i[11]+'万英镑')
        sheet1.write(row, 8, i[12])
        sheet1.write(row, 9, i[13]+'/'+i[14])
        sheet1.write(row, 10, i[15]+'/'+i[16])
        sheet1.write(row, 11, i[17])
        row=row+1

    row = 1
    for i in lineup2:
        sheet2.write(row, 0, i[1])
        sheet2.write(row, 1, i[2])
        sheet2.write(row, 2, i[5])
        sheet2.write(row, 3, i[6])
        sheet2.write(row, 4, i[7])
        sheet2.write(row, 5, i[8])
        sheet2.write(row, 6, i[9])
        if i[11]!='':
            sheet2.write(row, 7, i[11] + '万英镑')
        else:
            sheet2.write(row,7,'')
        sheet2.write(row, 8, i[12])
        sheet2.write(row, 9, i[13] + '/' + i[14])
        sheet2.write(row, 10, i[15] + '/' + i[16])
        sheet2.write(row, 11, i[17])
        row = row + 1
    wbk.save(r'haocai138_com/'+t1+'VS'+t2+'.xls')
def getteamid(all_id):
    team=[]
    headers={
        'Host':r'a.haocai138.com',
        'User-Agent': r'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.104 Safari/537.36 Core/1.53.4843.400 QQBrowser/9.7.13021.400',
    }
    url='http://a.haocai138.com'
    pattern1 = re.compile(r'hometeamid=\d+')
    pattern2 = re.compile(r'guestteamid=\d+')
    for match in all_id:
        r=requests.get(url+match,headers=headers)
        team_id=pattern1.search(r.text)
        team_id=team_id.group()
        home_team_id=team_id.split('=')[-1]
        team_id=pattern2.search(r.text)
        team_id=team_id.group()
        guest_team_id=team_id.split('=')[-1]
        team.append((home_team_id,guest_team_id))
    return team
if __name__=='__main__':

    all_id=getallid()
    print('14场比赛id为：',all_id)
    teamid=getteamid(all_id)
    print(teamid)
    if not os.path.exists('haocai138_com'):
        os.mkdir('haocai138_com')
        print('创建haocai138_com文件夹')

    for a in teamid:
        name,lineup1,lineup2=get2team(a)
        getxls(name,lineup1,lineup2)
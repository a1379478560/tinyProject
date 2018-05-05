import requests
import  xlwt
from  bs4 import BeautifulSoup
import os
def get_token():
    params={
        'client_id': 'ejS0TzdTjGaKUMqNSlA23PTb',
        'client_secret': 'idp2MPKhWb0ttiTrd7GvEnTYwVteDMmR',
        'grant_type': 'client_credentials'
    }
    token_url=r'https://aip.baidubce.com/oauth/2.0/token'
    headers={
        'Content-Type': 'application/json; charset=UTF-8',
    }
    r=requests.get(token_url, headers=headers, params=params)
    return r.json()['access_token']

def get_ocr(token,s):
    url='https://aip.baidubce.com/rest/2.0/ocr/v1/general_basic'
    image_url=r'http://c.spdex.com/ValidateCodePage.aspx'
    params={
        'access_token': token,
    }
    data={
        'url': image_url,
        'language_type':'ENG',
    }
    headers={
        'Content-Type': 'application/x-www-form-urlencoded',
    }
    r=requests.post(url,headers=headers,params=params,data=data)
    print(r.json())
    return r.json()

def login():
    image_url = r'http://c.spdex.com/ValidateCodePage.aspx'
    login_url=r'http://c.spdex.com/Login.aspx'
    headers={
        'Host':r'c.spdex.com',
        'Pragma': 'no-cache',
        'Cache-Control': 'no-cache',
        'Origin': r'http://c.spdex.com',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': r'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.104 Safari/537.36 Core/1.53.4843.400 QQBrowser/9.7.13021.400',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Accept':r'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Referer':r'http://c.spdex.com/Login.aspx?tip=1',
        'Accept-Encoding':'gzip, deflate',

    }

    s=requests.session()
    r=s.get(image_url)
    with open('验证码.jpg','wb+') as f:
        f.write(r.content)
    ocr=input('请输入验证码：')
    data={
        '__VIEWSTATE': r'/wEPDwULLTIwNjMwMjA1MDYPZBYCZg9kFgICBQ9kFgICAQ9kFgICAQ8PFgIeB1Zpc2libGVnZBYCAgEPDxYCHgRUZXh0BSrmgqjnmoTotKblj7flt7LlnKjlhbbku5blrqLmiLfnq6/nmbvlvZXvvIFkZGSpQ2pkhyMkYNjXIpISABOcPGWR6w==',
        '__VIEWSTATEGENERATOR':'C2EE9ABB',
        r'ctl00$ContentPlaceHolder1$TxtUserName':'aaaaaa22',
        r'ctl00$ContentPlaceHolder1$TxtPassWord':'aaaaaa22',
        r'ctl00$ContentPlaceHolder1$TxtValida':ocr,
        r'ctl00$ContentPlaceHolder1$BtnSubmit':'登 陆',
    }
    #ocr=get_ocr(get_token(),s)
    r=s.post(login_url,headers=headers,data=data)
    if r.url!=r'http://c.spdex.com/Members/Default.aspx' :
        soup=BeautifulSoup(r.text,'html.parser')
        print('登录失败，请重试！')
        print(soup.find('span', id='ContentPlaceHolder1_Lab1'))
        s=login()
    #print(r.text)
    print(r.status_code)
    #print(r.url)
    return s
#token=get_token()
#ocr=get_ocr(token)

def getallid(s):
    all_id=[]
    headers={
        'Host':r'c.spdex.com',
        'User-Agent': r'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.104 Safari/537.36 Core/1.53.4843.400 QQBrowser/9.7.13021.400',
    }
    origin_url=r'http://c.spdex.com'
    r=s.get(origin_url,headers=headers)
    soup=BeautifulSoup(r.text,'html.parser')
    origin_id=soup.find('ul',id='jcselect').find_all('a')[0].text
    print('今天的赛事编号是：',origin_id)
    url_temp=r'http://c.spdex.com/dv_'+ '1' + '_0_0_0_0_' +str(origin_id)
    r=s.get(url_temp,headers=headers)
    soup=BeautifulSoup(r.text,'html.parser')
    id=int(soup.find('div',{'class':'pagers'}).find_all('a')[-2].text)
    for i in range(1,id+1):
        url=r'http://c.spdex.com/dv_'+ str(i) + '_0_0_0_0_' +str(origin_id)
        r=s.get(url,headers=headers)
        soup=BeautifulSoup(r.text,'html.parser')
        all_id=all_id+list(map(f,soup.find_all('li',{'class': 'green'})))
        all_id_r=[]
        for iii in  all_id:
            if iii!=0:
                all_id_r.append(iii)
    return  all_id_r
def f(xx):
    if xx.text=='欧洲指数':
        return xx.find('a')['href']
    return  0
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
    url=r'http://c.spdex.com'
    #r=s.get(url+id,headers=headers)
    #soup=BeautifulSoup(r.text,'html.parser')
    #print(soup.find('title'))
    # try:
    #     n=soup.find('td',{'valign': 'bottom','nowrap': 'true',}).text[8:10]
    # except:
    #     print('这个没有数据')
    #     return
    # n=int(n)
    # print(n,'页','ok')
    wbk = xlwt.Workbook(encoding='ascii')
    sheet1 = wbk.add_sheet('sheet1')
    row=0
    r=s.get(url+id,headers=headers)
    soup=BeautifulSoup(r.text,'html.parser')
    tr=soup.find_all('tr',{'class': False})
    for x in tr:
        td=x.find_all('td')
        if len(td)==18 :
            sheet1.write(row,0,td[0].text)
            for col in range(1,18):
                sheet1.write(row,col,float(td[col].text))
            row=row+1
    wbk.save(r'spdex_com_ou_jingcai/'+str(ii)+'.xls')

if __name__=='__main__':
    s=login()
    all_id=getallid(s)
    print('所有比赛id为：',all_id)

    if not os.path.exists('spdex_com_ou_jingcai'):
        os.mkdir('spdex_com_ou_jingcai')
        print('创建spdex_文件夹')
    ii = 1  # 后面做文件名
    for a in range(len(all_id)):
        getxls(all_id[a],s,ii)
        ii=ii+1
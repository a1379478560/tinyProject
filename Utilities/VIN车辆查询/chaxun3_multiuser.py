import requests
from bs4 import BeautifulSoup
import xlrd
import xlwt
import time
import random
users=[
    ('CICPwh07', 'cic123'),
    ('CICPwh08', 'cic123'),
    ('CICPwh09', 'cic123'),
]


def readxls(fileName="1.xls"):
    data=[]
    try:
        wb=xlrd.open_workbook(fileName)
    except:
        print("打开文件失败，请检查文件名是否输入错误。")
        exit()
    sheet=wb.sheet_by_index(0)
    rows=sheet.nrows
    for row in range(1,rows):
        d=sheet.row_values(row)
        temp="0000"
        if type(d[0])==str and len(d[0])==17:
            data.append([d[0],temp])
        else:
            print("第",row+1,"行VIN码",d[0],"格式不对")
    return data

def getOne(session,vin):
    url="http://10.104.20.232:88/sinoiais/showall/query.do?dimensionSelect=02"
    header = {
        'User-Agent': r'Agent:Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.104 Safari/537.36 Core/1.53.4843.400 QQBrowser/9.7.13021.400',
        'Upgrade-Insecure-Requests': '1',
        'Referer': r'http://10.104.20.232:88/sinoiais/showall/query.do?dimensionSelect=02',
        # 'Cookie':'JSESSIONID=0001Law7FAwiRdWJw35gT6OMl1N:-18C2M72',
        'Origin': r'http://10.104.20.232:88',
        'Host': r'10.104.20.232:88',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Accept-Encoding': 'gzip, deflate',
        'Accept': "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
        'Accept-Language':'zh-CN,zh;q=0.9',
        'Cache-Control':'max-age=0',
        #'Cookie':'JSESSIONID=xybcqH_kOdf-96LToqXiGeC3unzSd3eGSxqQM_fyM7kMDuHCTsZL!1836396137',
    }
    params=[
        ('queryCredentialcode','01'),
        ('vin',vin),
        ( 'credentialcode',"01"),
        ('CheckboxGroup1', '02'),
        ('CheckboxGroup1', '05'),
        ('requestSource','http://10.192.0.36:80/flexitm/itm/product/result.jsp?vinflag=0'),
    ]
    try:
        #r=session.post(url=url,headers=header,data=params)
        r = session.post(url=url, headers=header, data=params)
        soup=BeautifulSoup(r.text,"html.parser")
        table1,table2=soup.find_all('table',)
        tr1=table1.find_all('tr')[1]
        tr2 = table2.find_all('tr')[1]
        td=tr1.find_all('td',)
        carId=tr2.find_all('td')[0].text
        due=tr1.find_all('td')[5].text
        engineNo = tr1.find_all('td')[9].text
        userName = tr1.find_all('td')[12].text
        print(carId,due,engineNo,userName)
        result=(vin,carId,due,engineNo,userName)
    except:
        print(vin,"未找到")
        result=(vin,"","","","")
    return result


def getSession(user):
    url = "http://10.104.20.232:88/sinoiais/checklogin/checkLoginInfo.do"
    session = requests.session()
    param = {
        "sysUserCode": user[0],
        'sysPassWord': user[1],
        'random': 'vhtx'
    }
    header = {
        'User-Agent': r'Agent:Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.104 Safari/537.36 Core/1.53.4843.400 QQBrowser/9.7.13021.400',
        'Upgrade-Insecure-Requests': '1',
        'Referer': r'http://10.104.20.232:88/sinoiais/',
        'Origin': r'http://10.104.20.232:88',
        'Host': r'10.104.20.232:88',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Accept-Encoding': 'gzip, deflate',
        'Accept': "application/json, text/javascript, */*; q=0.01",
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Cache-Control': 'max-age=0',
        # 'Cookie':'JSESSIONID=xybcqH_kOdf-96LToqXiGeC3unzSd3eGSxqQM_fyM7kMDuHCTsZL!1836396137',
    }
    t = int(time.time() * 1000)
    session.get(url="http://10.104.20.232:88/sinoiais/")
    randpic = session.get(url="http://10.104.20.232:88/sinoiais/pages/login/RandomNumUtil.jsp?d=" + str(t))
    with open("captcha.png", "wb") as f:
        f.write(randpic.content)
    vcode = input("输入验证码：")
    if vcode=='0':
        return '0'
    if vcode=='00':
        return '00'
    param['random'] = vcode
    r = session.post(url=url, data=param, headers=header)
    print("登录状态：",r.json()['msg'])
    if r.json()['msg']!="success":
        print("登录失败，请检查错误类型并重新登录！")
        session=getSession(user)
    return  session

def getAllSession(users):
    AllSession=[]
    loginNum=0
    for user in users:
        sess=getSession(user)
        if sess=='0':
            continue
        if sess=='00':
            break
        AllSession.append(sess)
        loginNum+=1
        print('{}登录成功，已登录{}个账号'.format(user[0],loginNum))
    return AllSession

def getAllitem(data):
    AllSession=getAllSession(users)
    print("登录完成！")
    print("开始查询！")
    res_list=[]
    for item in data:
        if item[1]=='0000':
            session=random.choice(AllSession)
            tmp=getOne(session,item[0])
            res_list.append(tmp)
    return res_list

def writexls(newData,saveFileName='result.xls'):
    wbk=xlwt.Workbook(encoding='ascii')
    sheet=wbk.add_sheet('查询结果')
    for i,x in enumerate(newData):
        sheet.write(i,0,x[0])
        sheet.write(i,1,x[1])
        sheet.write(i, 2, x[2])
        sheet.write(i, 3, x[3])
        sheet.write(i, 4, x[4])
    wbk.save(saveFileName)
    print("查询结果已经保存到",saveFileName)

#x=getOne(getsession(),'1LN6L9S98H5613768')
#print(x)



if __name__=='__main__':

    fileName=input("请输入文件名，默认1.xls")
    if fileName=='':
        data=readxls()
    else:
        data=readxls(fileName)
    print("共",len(data),"条有效记录")
    print("开始登录...")
    newData=getAllitem(data)
    print("查询完成，写入文件")
    writexls(newData)
    print("写入完成！")
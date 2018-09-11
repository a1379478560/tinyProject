import requests
import re
import xlwt
from bs4 import BeautifulSoup

def getMatchNumToday():
    url="http://www.500.com/"

    header2={
    'User-Agent': r'Agent:Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.104 Safari/537.36 Core/1.53.4843.400 QQBrowser/9.7.13021.400' ,
    }

    res=requests.get(url,headers=header2)
    pattern=re.compile(r'shuju-\d{6}.shtml')
    matchid=pattern.findall(res.text)
    pureNum=map(lambda x:x[6:12],matchid)
    return  list(pureNum)

def getMatchNum(id):
    url="http://www.500.com/static/public/sfc/daigou/xml/%s.xml" %(id)
    headers={
        'User-Agent': r'Agent:Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.104 Safari/537.36 Core/1.53.4843.400 QQBrowser/9.7.13021.400' ,
        "Accept-Encoding":"gzip, deflate",
        "Host":"www.500.com",
        "Referer":"http://www.500.com/",
        "X-Requested-With":"XMLHttpRequest",
    }
    res=requests.get(url=url,headers=headers)
    pattern=re.compile(r'fixtureid="\d{6}"')
    matchid=pattern.findall(res.text)
    pureNum=map(lambda x:x[11:17],matchid)
    return  list(pureNum)

def toInt(strNum):
    if ',' in strNum:
        strNum=strNum.replace(',','')

    if strNum[-1]=='%':
        num=float(strNum[0:-1])/100
        num=round(num+0.00001,3)
        return num
    if "." in strNum:
        try:
            num=float(strNum)
            return num
        except:
            return strNum
    try:
        num=int(strNum)
        return num
    except:
        return strNum

def getOnePageData(matchid):
    url="http://odds.500.com/fenxi/touzhu-%s.shtml"%(matchid)
    header = {
        'User-Agent': r'Agent:Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.104 Safari/537.36 Core/1.53.4843.400 QQBrowser/9.7.13021.400',
        'Upgrade-Insecure-Requests': '1',
        'Referer': url,
        'Host': r'odds.500.com',
        'Accept-Encoding': 'gzip, deflate',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    }
    res=requests.get(url=url,headers=header)
    res.encoding=res.apparent_encoding
    soup=BeautifulSoup(res.text,"html.parser")
    table=soup.find_all("table",{"class":"pub_table pl_table_data bif-yab"})[0]
    trs=table.find_all("tr")[2:5]
    data=[]
    for tr in trs:
        tds=tr.find_all("td")
        temp=[]
        for td in tds:
            temp.append(toInt(td.text))
        data.append(temp)

    comment=soup.find_all("em",{"class":"ying"})[0].text
    return  comment, data

def  writexls(data):
    global id
    wbk=xlwt.Workbook(encoding="ascii")
    sheet=wbk.add_sheet(id)
    for i,match in enumerate(data):
        row=6*i
        sheet.write(row,0,i+1)
        sheet.write(row+1,0,match[0])
        sheet.write(row + 1, 1, "赔率")
        sheet.write(row + 1, 2, "概率")
        sheet.write(row + 1, 3, "北单")
        sheet.write(row + 1, 4, "必发")
        sheet.write(row + 1, 5, "成交价")
        sheet.write(row + 1, 6, "成交量")
        sheet.write(row + 1, 7, "庄家盈亏")
        sheet.write(row + 1, 8, "必发指数")
        sheet.write(row + 1, 9, "冷热指数")
        sheet.write(row + 1, 10, "盈亏指数")

        print(match[1])
        for j in range(11):
            sheet.write(row+2,j,match[1][0][j])
        for j in range(11):
            sheet.write(row+3,j,match[1][1][j])
        for j in range(11):
            sheet.write(row+4,j,match[1][2][j])

    wbk.save("500_com结果.xls")

if __name__=="__main__":
    data=[]
    id=input("请输入要获取的期数，输入0获取当前期：")
    if id=="0" or len(id)<5:
        print("开始爬取今日数据...")
        matchId=getMatchNumToday()
    else:
        print("开始爬取第%s期数据...")
        matchId=getMatchNum(id)

    for i in matchId:
        temp=getOnePageData(i)
        data.append(temp)

    print("爬取完成，开始写入excel表格...")
    writexls(data)
    print("爬取完成！")

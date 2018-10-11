import requests
import re
import os
import time
import xlwt
from  bs4 import BeautifulSoup
from selenium import webdriver
id="2018126"
fileName = '310win_' + id + '.xls'
header={
'User-Agent': r'Agent:Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.104 Safari/537.36 Core/1.53.4843.400 QQBrowser/9.7.13021.400' ,
}
okpage=0

def getOnePage(id):
    timestamp=time.time()
    strTime=str(int(timestamp))+"000"
    url="http://www.310win.com/analysis/odds/"+id+"?"+strTime

    r=requests.get(url,headers=header)
    r.encoding=r.apparent_encoding
    soup=BeautifulSoup(r.text,"html.parser")
    div=soup.find("div",{"class":"bfDiv"})
    table=div.find_all("table")
    trs=table[0].find_all("tr",{"class":"tr_dl"})[3:]
    tableList1=[]
    for tr in trs :
        tds=tr.find_all("td")
        tdtemp=[]
        for td in tds:
            tdtemp.append(td.text)
        tableList1.append(tdtemp)
    trs2=table[1].find_all("tr",{"class":"odds"})
    tableList2 = []
    for tr in trs2:
        tds=tr.find_all("td")
        tdtemp=[]
        for td in tds:
            tdtemp.append(td.text)
        tableList2.append(tdtemp)
    global okpage
    okpage+=1
    ok="#"*okpage*2
    undo="="*(14-okpage)*2
    print("\r[{0}{1}] {2}/14".format(ok,undo,okpage),end="")
    return  [tableList1,tableList2]

def getMatchId(id):
    base_url="http://www.310win.com/buy/toto14.aspx?issueNum="+id
    r=requests.get(base_url,headers=header)
    pattern=re.compile(r'/analysis/\d{7}.htm')
    matchid=pattern.findall(r.text)
    return matchid

def getAllPageData():
    global id
    global fileName
    while True:
        id= input("请输入比赛期号：\n")
        if len(id)==7 and id.isdigit():
            break
        print("输入不合法，请输入七位纯数字期号。")
    fileName = '310win_' + id + '.xls'
    print("开始爬取数据...")
    time_start =time.time()
    matchIds=getMatchId(id)
    data=[]
    for matchId in matchIds:
        onePageData=getOnePage(matchId[-11:])
        data.append(onePageData)
    time_stop=time.time()
    time_delta=time_stop-time_start
    print("\n 总用时：{0}秒".format(round(time_delta,3)))
    return data

def writexls(data):
    global id
    wbk=xlwt.Workbook(encoding="ascii")
    sheet=wbk.add_sheet(str(id)+"期")
    for i,match in enumerate(data):
        base_row=9*i
        sheet.write(base_row+0,0,i+1)

        sheet.write(base_row + 1, 0, "选项")
        sheet.write(base_row + 1, 1, "赔率")
        sheet.write(base_row + 1, 2, "概率")
        sheet.write(base_row + 1, 3, "返还率")
        sheet.write(base_row + 1, 4, "价位")
        sheet.write(base_row + 1, 5, "概率")
        sheet.write(base_row + 1, 6, "返还率")
        sheet.write(base_row + 1, 7, "成交量")
        sheet.write(base_row + 1, 8, "成交比")
        sheet.write(base_row + 1, 9, "必发转换亚盘")
        sheet.write(base_row + 1, 10, "庄家盈亏")
        sheet.write(base_row + 1, 11, "盈亏指数")
        sheet.write(base_row + 1, 12, "冷热指数")

        sheet.write(base_row + 5, 0, "选项")
        sheet.write(base_row + 5, 1, "买家挂牌")
        sheet.write(base_row + 5, 2, "赔率")
        sheet.write(base_row + 5, 3, "卖家挂牌")
        sheet.write(base_row + 5, 4, "赔率")
        sheet.write(base_row + 5, 5, "成交额")
        sheet.write(base_row + 5, 6, "赔率")
        sheet.write(base_row + 5, 7, "成交比例")
        sheet.write(base_row + 5, 8, "庄家盈亏")
        sheet.write(base_row + 5, 9, "冷热指数")
        sheet.write(base_row + 5, 10, "必发指数")
        sheet.write(base_row + 5, 11, "盈亏指数")
        #print(match[0])
        #print("**************************************")

        #print(match[0])
        for j in range(13):
            sheet.write(base_row+2,j,match[0][0][j])  #主队
            sheet.write(base_row + 3, j, match[0][1][j])#平局
            sheet.write(base_row+4,j,match[0][2][j]) # 客队
        for  j in range(12):
            sheet.write(base_row+6,j,match[1][0][j])
            sheet.write(base_row+7,j,match[1][1][j])


        wbk.save(fileName)

def s_int(n):
    try:
        return int(n)
    except:
        return 0

def s_float(n):
    try:
        return float(n)
    except:
        return 0

def procdata(data):
    for match in data:

        match[0][1].insert(3,match[0][0][3]) #拆分单元格
        match[0][2].insert(3,match[0][0][3])
        match[0][1].insert(6,match[0][0][6])
        match[0][2].insert(6,match[0][0][6])

        for  i in range(3):
            match[0][i][1]=s_float(match[0][i][1])
            match[0][i][2]=s_float(match[0][i][2].replace("%",""))/100
            match[0][i][3] = s_float(match[0][i][3].replace("%",""))/100
            match[0][i][4] = s_float(match[0][i][4])
            match[0][i][5] = s_float(match[0][i][5].replace("%", "")) / 100
            match[0][i][6] = s_float(match[0][i][6].replace("%", "")) / 100
            match[0][i][7] = s_int(match[0][i][7].replace(",",""))
            match[0][i][8] = s_float(match[0][i][8].replace("%", "")) / 100
            match[0][i][10] = s_int(match[0][i][10])
            match[0][i][11] = s_int(match[0][i][11])
            match[0][i][12] = s_int(match[0][i][12])
        for i in range(2):
            match[1][i][1]=s_int(match[1][i][1].replace(",",""))
            match[1][i][2] = s_float(match[1][i][2])
            match[1][i][3] = s_int(match[1][i][3].replace(",", ""))
            match[1][i][4] = s_float(match[1][i][4])
            match[1][i][5] = s_int(match[1][i][5].replace(",", ""))
            match[1][i][6] = s_float(match[1][i][6])
            match[1][i][7] = s_float(match[1][i][7].replace("%", "")) / 100
            match[1][i][8] = s_int(match[1][i][8])
            match[1][i][9] = s_int(match[1][i][9])
            match[1][i][10] = s_int(match[1][i][10])
            match[1][i][11] = s_int(match[1][i][11])
    return data

if __name__ == '__main__':
    data=getAllPageData()
    print("数据爬取完成，开始格式化数据...")
    data=procdata(data)
    print("格式化完成，写入文件...")
    writexls(data)
    print("成功写入文件到",fileName)
import requests
import re
import os
import time
import xlwt
from  bs4 import BeautifulSoup
from selenium import webdriver

filePath='300win_com/'
header={
'User-Agent': r'Agent:Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.104 Safari/537.36 Core/1.53.4843.400 QQBrowser/9.7.13021.400' ,
}

def getxls(matchId):
    wbk=xlwt.Workbook(encoding='ascii')
    sheet1 = wbk.add_sheet('即时盘')
    sheet2 = wbk.add_sheet('初盘')
    url1 = geturl(matchId)
    url2 =url1[0:-2]+str(2)
    r1=requests.get(url1,headers=header)
    soup=BeautifulSoup(r1.text,'html.parser')
    td=soup.find('td')
    a=td.find_all('a')
    fileName=a[0].string+'VS'+a[1].string
    print(fileName)
    trs=soup.find_all('tr',{'bgcolor':'#FFFFFF'})
    for raw,tr in enumerate(trs):
        tds=tr.find_all('td')
        sheet1.write(raw,0,tds[0].string)
        sheet1.write(raw, 1, float(tds[1].string))
        sheet1.write(raw, 2, float(tds[2].string))
        sheet1.write(raw, 3, float(tds[3].string))
        sheet1.write(raw, 4, round(float(tds[4].string[0:-1])/100,4))
        sheet1.write(raw, 5, float(tds[5].string))
        sheet1.write(raw, 6, tds[6].string)
        sheet1.write(raw, 7, float(tds[7].string))
        sheet1.write(raw, 8, float(tds[8].string))


    time.sleep(1)
    r2=requests.get(url2,headers=header)
    soup2=BeautifulSoup(r2.text,'html.parser')
    trs=soup2.find_all('tr',{'bgcolor':'#FFFFFF'})
    for raw,tr in enumerate(trs):
        tds=tr.find_all('td')
        sheet2.write(raw,0,tds[0].string)
        sheet2.write(raw, 1, float(tds[1].string))
        sheet2.write(raw, 2, float(tds[2].string))
        sheet2.write(raw, 3, float(tds[3].string))
        sheet2.write(raw, 4, round(float(tds[4].string[0:-1])/100,4))
        sheet2.write(raw, 5, float(tds[5].string))
        sheet2.write(raw, 6, tds[6].string)
        sheet2.write(raw, 7, float(tds[7].string))
        sheet2.write(raw, 8, float(tds[8].string))
    wbk.save(filePath+fileName+'.xls')

def getMatchId(url):
    r=requests.get(url,headers=header)
    pattern=re.compile(r'/1x2/\d{7}.html')
    matchid=pattern.findall(r.text)
    return matchid

def geturl(uri):
    url='http://www.310win.com/1x2/'+uri+'.html'
    browser = webdriver.PhantomJS()   #需要已将phantomjs.exe放入python的Scripts文件夹下
    #browser = webdriver.Chrome(r'E:/chromedriver.exe')
    browser.get(url)
    curent_page = browser.current_window_handle
    browser.find_element_by_xpath('//input[@name="chkall"]').click()  # click
    browser.find_element_by_xpath('//a[@onclick="exChange();return false;"]').click()
    handles = browser.window_handles

    for handle in handles:  # 切换窗口
        if handle != browser.current_window_handle:
            print('switch to ', handle)
            browser.switch_to_window(handle)
            print(browser.current_window_handle)  # 输出当前窗口句柄
            break
    result_url=browser.current_url
    time.sleep(5)
    for handle in handles:
            browser.switch_to_window(handle)
            browser.close()
    return result_url
if  __name__=='__main__':
    id=input('请输入要爬取的期号：\n')
    url='http://www.310win.com/buy/toto14.aspx?issueNum='+str(id)
    matchId=getMatchId(url)

    if not os.path.exists(filePath):
        os.mkdir(filePath)
        print('创建300win_com文件夹')
    for i in matchId:
        print(i[5:12])
        getxls(i[5:12])
        print(i,'ok...')
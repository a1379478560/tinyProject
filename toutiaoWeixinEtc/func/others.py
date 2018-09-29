import requests
from bs4 import BeautifulSoup
import time
from datetime import datetime
from  datetime import timedelta
import re
HEADERS = {
    'User-Agent': r'Agent:Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.104 Safari/537.36 Core/1.53.4843.400 QQBrowser/9.7.13021.400',
}
def getPermnertUrl(origin):
    r=requests.get(origin,headers=HEADERS)
    time.sleep(1)
    return r.url

def arctical_filter(arcticals):
    article_new=[]
    WORD_LIST = ["Flyme", "flyme", ]
    patterns = []
    for word in WORD_LIST:
        patterns.append(re.compile(word))

    for arctical in arcticals:
        try:
            url=arctical['article']['url']
        except:
            url=arctical['article_url']
        r=requests.get(url,headers=HEADERS)
        flag = 0
        for pattern in patterns:
            flag+=len(pattern.findall(r.text))
        if flag>=4:
            article_new.append(arctical)
    return article_new

def strToTime(time_str):
    if "天前" in time_str:
        time_str=time_str.replace("天前","")
        time_str=int(time_str)
        date= datetime.now()-timedelta(days=time_str)
        date_str=date.strftime('%Y-%m-%d')
        return date_str
        return
    if "小时前" in  time_str:
        time_str=time_str.replace("小时前","")
        time_str=int(time_str)
        date=datetime.now()-timedelta(hours=time_str)
        date_str=date.strftime('%Y-%m-%d')
        return date_str
    return time_str

def qudong():
    url='https://app.qudong.com/?app=search&controller=index&action=search&wd=flyme&page=1&type=article&order=time'
    r=requests.get(url,headers=HEADERS)
    r.encoding=r.apparent_encoding
    soup=BeautifulSoup(r.text,"html.parser")
    lis=soup.find_all('li',{'class':"article-picture-item"})
    data=[]
    for li in lis :
        temp={}
        keyword=li.find('span',{"class":"keyword"})
        if keyword:
            temp['title']=li.find('h3').text
            temp['url']=li.find('a')['href']
            temp['date']=li.find('div').find('div').find('span').text
            temp['platform']="驱动之家"
            temp["channel"]="手机"
            temp['date'] = strToTime(temp['date'])
            temp['abstract']=temp['title']
            data.append(temp)
    return data

def ithome():
    url="http://so.ithome.com/cse/search?q=flyme&s=10375816656400526905&srt=lds&stp=1&sti=10080&nsid=0"
    url_baidu="https://www.baidu.com/s?ie=utf-8&f=8&rsv_bp=1&rsv_idx=1&tn=baidu&wd=title%3A%20(%20%22flyme%22%20)%20site%3A(ithome.com)&oq=title%253A%2520(%2520%2526quot%253Bflyme%2526quot%253B%2520)%2520site%253A(ithome.com)&rsv_pq=f5d374a700003f29&rsv_t=a8c9oorelDdpb4slh%2FM0qizZv1BInCSSRylzcUl0Mt4viGjzCM%2BiJ50kofw&rqlang=cn&rsv_enter=0&gpc=stf%3D1536892522%2C1537497322%7Cstftype%3D1&tfflag=1&si=(ithome.com)&ct=2097152&rsv_srlang=cn&sl_lang=cn&rsv_rq=cn"
    r=requests.get(url_baidu,headers=HEADERS)
    r.encoding=r.apparent_encoding
    soup=BeautifulSoup(r.text,"html.parser")
    divs = soup.find_all('div', {'class': "result c-container "})
    data=[]
    for div in divs:
        temp={}
        temp['url']=div.find('h3').find('a')['href']
        title=div.find('h3').find('a').text.split("-")
        try:
            temp['platform']=title[2]
            if "..." in temp['platform']:
                temp['platform']="IT之家"
        except:
            temp['platform'] = "IT之家"
        try:
            temp['channel']=title[1]
        except:
            temp['channel'] = "业界动态"
        temp['title']=title[0]
        temp["date"]=div.find('span',{"class":' newTimeFactor_before_abs m'}).text
        temp['abstract']=div.find('div',{"class":"c-abstract"}).text
        temp["date"]=div.find('span',{"class":' newTimeFactor_before_abs m'}).text.replace("\xa0-\xa0",'')
        temp['abstract']=div.find('div',{"class":"c-abstract"}).text.split('\xa0-\xa0')[-1]
        temp['date'] = strToTime(temp['date'])
        temp['url'] = getPermnertUrl(temp['url'])
        data.append(temp)
    return data

def chinaz():
    url_baidu="https://www.baidu.com/s?q1=flyme&q2=&q3=&q4=&gpc=stf%3D1536899588.7%2C1537504388.7%7Cstftype%3D1&ft=&q5=1&q6=chinaz.com&tn=baiduadv"
    r=requests.get(url_baidu,headers=HEADERS)
    r.encoding=r.apparent_encoding
    soup=BeautifulSoup(r.text,"html.parser")
    divs = soup.find_all('div', {'class': "result c-container "})
    data=[]
    for div in divs:
        temp={}
        temp['url']=div.find('h3').find('a')['href']
        title=div.find('h3').find('a').text.split("-")
        temp['platform'] = "站长之家"
        temp['channel'] = "传媒"
        temp['title']=title[0]
        temp["date"]=div.find('span',{"class":' newTimeFactor_before_abs m'}).text
        temp['abstract']=div.find('div',{"class":"c-abstract"}).text
        temp["date"]=div.find('span',{"class":' newTimeFactor_before_abs m'}).text.replace("\xa0-\xa0",'')
        temp['abstract']=div.find('div',{"class":"c-abstract"}).text.split('\xa0-\xa0')[-1]
        temp['url'] = getPermnertUrl(temp['url'])
        temp['date'] = strToTime(temp['date'])
        data.append(temp)
    return data

def techweb():
    url_baidu="https://www.baidu.com/s?q1=flyme&q2=&q3=&q4=&gpc=stf%3D1536899588.7%2C1537504388.7%7Cstftype%3D1&ft=&q5=1&q6=techweb.com.cn&tn=baiduadv"
    r=requests.get(url_baidu,headers=HEADERS)
    r.encoding=r.apparent_encoding
    soup=BeautifulSoup(r.text,"html.parser")
    divs = soup.find_all('div', {'class': "result c-container "})
    data=[]
    for div in divs:
        temp={}
        temp['url']=div.find('h3').find('a')['href']
        title=div.find('h3').find('a').text.split("-")
        temp['platform'] = "techweb"
        temp['channel'] = "资讯"
        temp['title']=title[0]
        temp["date"]=div.find('span',{"class":' newTimeFactor_before_abs m'}).text.replace("\xa0-\xa0",'')
        temp['abstract']=div.find('div',{"class":"c-abstract"}).text.split('\xa0-\xa0')[-1]
        temp['url'] = getPermnertUrl(temp['url'])
        temp['date'] = strToTime(temp['date'])
        data.append(temp)
    return data

def yesky():
    url_baidu="https://www.baidu.com/s?ie=utf-8&f=8&rsv_bp=1&tn=baiduadv&wd=title%3A%20(flyme)&oq=site%3A(chinaz.com)%20title%3A%20(flyme)&rsv_pq=e726b1ef0000c15b&rsv_t=718ewxhnd%2F2BDfL4KMJ8ZFGXHY7xDfi0WJYMuU%2FXQvG%2F%2B90%2Bw11pxXc76ToHuE8&rqlang=cn&rsv_enter=1&si=yesky.com&ct=2097152&gpc=stf%3D1536891917.265%2C1537496717.265%7Cstftype%3D1&rsv_srlang=cn&sl_lang=cn&rsv_rq=cn"
    r=requests.get(url_baidu,headers=HEADERS)
    r.encoding=r.apparent_encoding
    soup=BeautifulSoup(r.text,"html.parser")
    divs = soup.find_all('div', {'class': "result c-container "})
    data=[]
    for div in divs:
        temp={}
        temp['url']=div.find('h3').find('a')['href']
        title=div.find('h3').find('a').text.split("-")
        temp['platform'] = "天极网"
        temp['channel'] = "IT新闻"
        temp['title']=title[0]
        temp["date"]=div.find('span',{"class":' newTimeFactor_before_abs m'}).text.replace("\xa0-\xa0",'')
        temp['abstract']=div.find('div',{"class":"c-abstract"}).text.split('\xa0-\xa0')[-1]
        temp['url'] = getPermnertUrl(temp['url'])
        temp['date'] = strToTime(temp['date'])
        data.append(temp)
    return data

def ifeng():
    url_baidu="https://www.baidu.com/s?ie=utf-8&f=8&rsv_bp=1&tn=baiduadv&wd=title%3A%20(flyme)&oq=site%3A(chinaz.com)%20title%3A%20(flyme)&rsv_pq=e726b1ef0000c15b&rsv_t=c3e23KqEJaVvDzHsxsFCTv5bT3Y8b9p9pPRoNqDerEirNKkMGa1i931OJUTwhCA&rqlang=cn&rsv_enter=1&si=ifeng.com&ct=2097152&gpc=stf%3D1536891917.265%2C1537496717.265%7Cstftype%3D1&rsv_srlang=cn&sl_lang=cn&rsv_rq=cn"
    r=requests.get(url_baidu,headers=HEADERS)
    r.encoding=r.apparent_encoding
    soup=BeautifulSoup(r.text,"html.parser")
    divs = soup.find_all('div', {'class': "result c-container "})
    data=[]
    for div in divs:
        temp={}
        temp['url']=div.find('h3').find('a')['href']
        title=div.find('h3').find('a').text.split("-")
        temp['platform'] = "凤凰网"
        temp['channel'] = "科技"
        temp['title']=title[0]
        temp["date"]=div.find('span',{"class":' newTimeFactor_before_abs m'}).text.replace("\xa0-\xa0",'')
        temp['abstract']=div.find('div',{"class":"c-abstract"}).text.split('\xa0-\xa0')[-1]
        temp['url'] = getPermnertUrl(temp['url'])
        temp['date']=strToTime(temp['date'])
        data.append(temp)
    return data

def anzhuo():
    url_baidu="https://www.baidu.com/s?q1=title%3A+%28Flyme%29&q2=&q3=&q4=&gpc=stf%3D1536901746.762%2C1537506546.762%7Cstftype%3D1&ft=&q5=&q6=anzhuo.cn&tn=baiduadv"
    r=requests.get(url_baidu,headers=HEADERS)
    r.encoding=r.apparent_encoding
    soup=BeautifulSoup(r.text,"html.parser")
    divs = soup.find_all('div', {'class': "result c-container "})
    data=[]
    for div in divs:
        temp={}
        temp['url']=div.find('h3').find('a')['href']
        title=div.find('h3').find('a').text.split("-")
        temp['platform'] = "安卓中国"
        temp['channel'] = "科技"
        temp['title']=title[0]
        temp["date"]=div.find('span',{"class":' newTimeFactor_before_abs m'}).text.replace("\xa0-\xa0",'')
        temp['abstract']=div.find('div',{"class":"c-abstract"}).text.split('\xa0-\xa0')[-1]
        temp['url'] = getPermnertUrl(temp['url'])
        temp['date'] = strToTime(temp['date'])
        data.append(temp)
    return data

def getAll():
    data=[]
    domains=[(ifeng,"凤凰网"),(anzhuo,"安卓之家"),(yesky,"天极网"),(techweb,"TechWeb"),(chinaz,"站长之家"),(qudong,"驱动之家"),(ithome,"IT之家"),]
    for domain in domains:
        print("开始爬取",domain[1])
        try:
            tempData=domain[0]()
        except:
            #raise
            print("爬取",domain[1],"失败，可能是因为网络不佳，若同一个网址多次爬取失败可能是因为网站改版。")
            tempData=[]
        if tempData:
            data.extend(tempData)
    return data

if __name__ == '__main__':
    data=getAll()
    print(data)












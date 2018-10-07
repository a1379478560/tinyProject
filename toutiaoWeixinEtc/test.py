from func.others import getAll
from func.others import arctical_filter
import requests

from bs4 import BeautifulSoup
import time
from datetime import datetime
from  datetime import timedelta
import re
def anzhuo():
    url_baidu="https://www.baidu.com/s?q1=title%3A+%28Flyme%29&q2=&q3=&q4=&gpc=stf%3D"+now+".762%2C"+weekago+".762%7Cstftype%3D1&ft=&q5=&q6=anzhuo.cn&tn=baiduadv"
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


# import time
# now=int(time.time())
# weekago=now-604800
# print(now)
# print(weekago)

# import  wechatsogou
# import re
# import requests
# HEADERS = {
#     'User-Agent': r'Agent:Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.104 Safari/537.36 Core/1.53.4843.400 QQBrowser/9.7.13021.400',
# }
# def arctical_filter(arcticals):
#     article_new=[]
#     WORD_LIST = ["Flyme", "flyme", ]
#     patterns = []
#     for word in WORD_LIST:
#         patterns.append(re.compile(word))
#
#     for arctical in arcticals:
#         url=arctical['article']['url']
#         r=requests.get(url,headers=HEADERS)
#         flag = 0
#         for pattern in patterns:
#             flag+=len(pattern.findall(r.text))
#             print(flag)
#         if flag>=3:
#             article_new.append(arctical)
#         print("*****************************************")
#     return article_new
#
# ws_api = wechatsogou.WechatSogouAPI()
# onePageData = ws_api.search_article('flyme', page=1, timesn=2, )
# print(len(onePageData))
# a=arctical_filter(onePageData)
# print(len(a))
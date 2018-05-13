# -*- coding:utf-8 -*-
import requests
from bs4 import BeautifulSoup
import os
import json
id=1
headers = {
    'Cache-Control': 'no-cache',
    'User-Agent': r'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.104 Safari/537.36 Core/1.53.4843.400 QQBrowser/9.7.13021.400',

}
def getAllUrl(url):
    all_url={}
    r=requests.get(url,headers=headers)
    soup=BeautifulSoup(r.text,'html.parser')
    ul=soup.find_all('ul', {'class':"index-category cicon"})[1]
    li_all=ul.find_all('li')
    for li in li_all:
        all_url[li.find('a')['href']]=(li.find('a').find('i')['class'][0],li.find('a').text)
    return all_url

def getappdata(path,cat_name,max_page=1):
    global id
    r_json={}
    r_list=[]
    url='https://apkpure.com'+path
    for ii in range(1,max_page+1):
        try:
            r=requests.get(url,params={'page':str(ii),'ajax':'1'},headers=headers)
            soup=BeautifulSoup(r.text,'html.parser')
            lis=soup.find_all('li')
            for li in lis:
                div=li.find('div',{'class':'category-template-img'})
                name=div.find('a')['title']
                package_name=div.find('a')['href'].split('/')[-1]
                item={
                    "id":id,
                    "appName":'',
                    "packageName":package_name,
                    #"classType":cat_name[0]
                    "classType":path.split('/')[-1]
                }

                id=id+1
                r_list.append(item)
        except:
            break
    r_json["RECORDS"]=r_list
    if not os.path.exists('results'):
        os.mkdir('results')
    json_ob=json.dumps(r_json,sort_keys=True,indent=4)
#    json_ob=eval('u'+"\'"+json_ob+"\'")
    with open('results/'+cat_name[1]+'.json','w') as f:
        f.write(json_ob)
    print(cat_name[1],'ok')
if __name__=='__main__':
    apkpure_com_url='https://apkpure.com/cn/art_and_design'
    all_url=getAllUrl(apkpure_com_url)
    for path in all_url:
        getappdata(path,all_url[path],max_page=100)     # max_page参数可以设置每个类别抓取的app个数，每个page=20个app




import pymysql
import requests
from bs4 import BeautifulSoup
import os
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

def connectdb():
    try:
        db=pymysql.connect('140.143.143.164','ferris','123456','launcher')
        cursor=db.cursor()
        print('数据库连接成功！')
        cursor.execute('SELECT VERSION()')
    except:
        print('数据库连接失败，请检查')
    return db

def insertraw(db,appName,classType,packageName):
    cursor=db.cursor()
    sql="INSERT INTO appclass_test(appName, classType,packageName) VALUES('%s', '%s','%s');" %(appName,classType,packageName)
    print(sql)
    try:
        cursor.execute(sql)
        db.commit()
    except pymysql.err.IntegrityError:
        print('重复数据')
        db.rollback()
    except:
        #raise
        print('插入失败')
        db.rollback()

def getappdata(db,path,cat_name,max_page=1):
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
                    #"appName": name,
                    "appName":'',
                    "packageName":package_name,
                    "classType":path.split('/')[-1]
                }
                insertraw(db,item['appName'],item['classType'],item['packageName'])
        except:
            #raise
            print(path,'有失败项')
            break

if __name__=='__main__':
    db=connectdb()
    apkpure_com_url = 'https://apkpure.com/cn/art_and_design'
    all_url = getAllUrl(apkpure_com_url)
    print(all_url)
    for path in all_url:
        print(all_url[path][1],'开始')
        getappdata(db,path,all_url[path],max_page=100)     # max_page参数可以设置每个类别抓取的app个数，每个page=20个app
        print(all_url[path][1],'ok')
    db.close()
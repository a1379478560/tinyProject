import requests
import json
import time
import xlwt
import wechatsogou
from func.others import getAll
from func.others import arctical_filter
FIND_TIME=7
KEY_WORD='flyme'
HEADERS = {
    'User-Agent': r'Agent:Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.104 Safari/537.36 Core/1.53.4843.400 QQBrowser/9.7.13021.400',
}

def getToutiaoOnePageArctical(offset, keyword):
    params = {
        'offset': offset,
        'format': 'json',
        'keyword': keyword,
        'autoload': 'true',
        'count': '20',
        'cur_tab': 1,
        'from': 'search_tab'
    }
    url = 'https://www.toutiao.com/search_content/'
    data = []
    try:
        r = requests.get(url,headers = HEADERS,params=params)
        jsontext = json.loads(r.text)
        for x in jsontext['data']:
            if 'open_url' in x:
                if time.time() - int(x['create_time']) > FIND_TIME * 24 * 3600:  # 剔除时间不符合的
                    continue
                temp = {}
                temp['datetime'] = x['datetime']
                temp['media_name'] = x['media_name']
                temp['title'] = x['title']
                temp['abstract'] = x['abstract']
                temp['article_url'] = "http://toutiao.com"+x['open_url']
                temp['comments_count'] = x['comments_count']
                data.append(temp)
        return data
    except:
        return data

def  getToutiao():
    data=[]
    for i in range(10):
        temp=getToutiaoOnePageArctical(i*20,KEY_WORD)
        data+=temp
        #print(i)
        time.sleep(1)
    print(len(data))
    data=arctical_filter(data)
    print(len(data))
    return data

def writeToutiao(sheet,toutiaodata):
    row = 0
    sheet.write(row, 0, '序号')
    sheet.write(row, 1, '时间')
    sheet.write(row, 2, '作者')
    sheet.write(row, 3, '标题')
    sheet.write(row, 4, '主要信息')
    sheet.write(row, 5, '舆情类型')
    sheet.write(row, 6, '作者观念')
    sheet.write(row, 7, '链接')
    sheet.write(row, 8, '评论量')
    sheet.write(row, 9, '类型')
    sheet.write(row, 10, '备注')
    for arctical in toutiaodata:
        row+=1
        sheet.write(row,0,row)
        sheet.write(row,1,arctical['datetime'])
        sheet.write(row, 2, arctical['media_name'])
        sheet.write(row, 3, arctical['title'])
        sheet.write(row, 4, arctical['abstract'])
        sheet.write(row, 5, "")
        sheet.write(row, 6, arctical['title'])
        sheet.write(row, 7, arctical['article_url'])
        sheet.write(row, 8, arctical['comments_count'])
        sheet.write(row, 9, "")
        sheet.write(row, 10, "")
    return sheet

def writeWeixin(sheet,data):
    row = 0
    sheet.write(row, 0, '序号')
    sheet.write(row, 1, '时间')
    sheet.write(row, 2, '作者')
    sheet.write(row, 3, '标题')
    sheet.write(row, 4, '主要信息')
    sheet.write(row, 5, '舆情类型')
    sheet.write(row, 6, '作者观念')
    sheet.write(row, 7, '链接')
    for arctical in data:
        row += 1

        timeStamp = int(arctical['article']['time'])
        timeArray = time.localtime(timeStamp)
        date = time.strftime("%Y-%m-%d", timeArray)

        sheet.write(row, 0, row)
        sheet.write(row, 1, date)
        sheet.write(row, 2, arctical['gzh']['wechat_name'])
        sheet.write(row, 3, arctical['article']['title'])
        sheet.write(row, 4, arctical['article']['abstract'])
        sheet.write(row, 5, "")
        sheet.write(row, 6, arctical['article']['title'])
        sheet.write(row, 7, arctical['article']['url'])

    return sheet

def weiteOthers(sheet,data):
    row = 0
    sheet.write(row, 0, '序号')
    sheet.write(row, 1, '时间')
    sheet.write(row, 2, '平台')
    sheet.write(row, 3, '频道')
    sheet.write(row, 4, '标题')
    sheet.write(row,5,"主要信息")
    sheet.write(row, 6, '舆情类型')
    sheet.write(row, 7, '作者观念')
    sheet.write(row, 8, '链接')
    for arctical in data:
        row += 1
        sheet.write(row, 0, row)
        sheet.write(row, 1, arctical['date'])
        sheet.write(row, 2, arctical['platform'])
        sheet.write(row, 3, arctical['channel'])
        sheet.write(row, 4, arctical['title'])
        sheet.write(row, 5, arctical['title'])
        sheet.write(row, 6, "")
        sheet.write(row, 7, arctical['title'])
        sheet.write(row,8,arctical['url'])

    return sheet

def writexls(data):
    wkb=xlwt.Workbook(encoding='ascii')
    sheet_toutiao=wkb.add_sheet("今日头条")
    sheet_wx=wkb.add_sheet("微信")
    sheet_other=wkb.add_sheet("平面&网媒")
    writeToutiao(sheet_toutiao,data[0])
    writeWeixin(sheet_wx,data[1])
    weiteOthers(sheet_other,data[2])
    try:
        wkb.save("r.xls")
    except:
        wkb.save("r1.xls")

def getOnePageWeixin(keyword,page):
    base_url = 'http://weixin.sogou.com/weixin?'
    headers = {
        'Cookie': 'ABTEST=0|1537437347|v1; SUID=C0252F3B6E2F940A000000005BA36EA3; SUID=652948DF3921940A000000005BA36EA3; weixinIndexVisited=1; SUV=00FB4F753B2F25C05BA36EA4583A9089; Hm_lvt_ba7c84ce230944c13900faeba642b2b4=1537437350; SNUID=ED0903162C295A66AA5E46652DA8906F; JSESSIONID=aaazTqRDqVZEH4aLeWBvw; IPLOC=CN2104; Hm_lpvt_ba7c84ce230944c13900faeba642b2b4=1537437367',
        'Host': 'weixin.sogou.com',
        'Upgrade-Insecure-Requests': '1',
        'Referer':'http://weixin.sogou.com/weixin?type=2&query=flyme&ie=utf8&s_from=input&_sug_=y&_sug_type_=',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36'
    }
    params = {
        'query': keyword,
        'type': 2,
        'page': page,
        'ie':'utf8',
        's_from':'input',
        '_sug_':'n',
        'tsn':"2",         #tsn=2代表一周内的新闻
        '_sug_type_':'',
    }
    try:
        r=requests.get(base_url,headers=headers,params=params)
        r.encoding=r.apparent_encoding
        return r.text
    except:
        print("can't get html")
        return None

def getAllPageWeixin():
    data=[]
    ws_api = wechatsogou.WechatSogouAPI()
    for i in range(1,10):
        onePageData = ws_api.search_article('flyme', page=i, timesn=2, )
        if onePageData :
            data.extend(onePageData)
        if len(onePageData)<10:
            break
        time.sleep(1)
    temp=[]
    for x in data:
        if '吉他' not in x['gzh']['wechat_name']:    #有一个吉他乐队跟flyme重名了，过滤掉它
            temp.append(x)
    temp=arctical_filter(temp)
    return temp

if __name__ == '__main__':
    print("开始抓取今日头条")
    try:
        toutiao_data=getToutiao()
    except:
        print("抓取今日头条失败，可能是因为网络不佳，若同一个网址多次爬取失败可能是因为网站改版。")
        toutiao_data=[]
    print("开始抓取微信公众号")
    try:
        WeixinData=getAllPageWeixin()
    except:
        print("抓取微信公众号文章失败，可能是因为网络不佳，若同一个网址多次爬取失败可能是因为网站改版。")
        WeixinData=[]
    otherData=getAll()
    all_data=[toutiao_data,WeixinData,otherData]
    print("抓取完毕，开始保存到Excel文件，文件为当前目录下的r.xls")
    writexls(data=all_data)
    print("保存成功！")

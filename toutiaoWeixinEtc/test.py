import  wechatsogou
import re
import requests
HEADERS = {
    'User-Agent': r'Agent:Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.104 Safari/537.36 Core/1.53.4843.400 QQBrowser/9.7.13021.400',
}
def arctical_filter(arcticals):
    article_new=[]
    WORD_LIST = ["Flyme", "flyme", ]
    patterns = []
    for word in WORD_LIST:
        patterns.append(re.compile(word))

    for arctical in arcticals:
        url=arctical['article']['url']
        r=requests.get(url,headers=HEADERS)
        flag = 0
        for pattern in patterns:
            flag+=len(pattern.findall(r.text))
            print(flag)
        if flag>=3:
            article_new.append(arctical)
        print("*****************************************")
    return article_new

ws_api = wechatsogou.WechatSogouAPI()
onePageData = ws_api.search_article('flyme', page=1, timesn=2, )
print(len(onePageData))
a=arctical_filter(onePageData)
print(len(a))
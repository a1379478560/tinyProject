import requests
HEADERS = {
    'User-Agent': r'Agent:Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.104 Safari/537.36 Core/1.53.4843.400 QQBrowser/9.7.13021.400',
}
url='https://www.baidu.com/s?ie=utf-8&f=8&rsv_bp=1&tn=baiduadv&wd=site%3A(qudong.com)%20title%3A%20(flyme)&oq=site%253A(qudong.com)%2520title%253A%2520(flyme1)&rsv_pq=9942f4930004d878&rsv_t=c572UVRpx0MN%2FnC1wU71ugPPHBy8q8VAXEqo3qY%2BrQhYaSWp4s0b7%2FyN5l09o7o&rqlang=cn&rsv_enter=0&inputT=1895&gpc=stf%3D1536886211%2C1537491011%7Cstftype%3D1&tfflag=1&si=(qudong.com)&ct=2097152&rsv_srlang=cn&sl_lang=cn&rsv_rq=cn'
r=requests.get(url,headers=HEADERS)
print(r.text)
import requests
from bs4 import BeautifulSoup
import  os
#coding=utf-8

header = {
    "Accept-Encoding": "utf-8",
    'User-Agent':'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6'
}

def decode_chunked(content):
    content = content.lstrip('\r')
    content = content.lstrip('\n')
    temp = content.find('\r\n')
    strtemp = content[0:temp]
    readbytes = int(strtemp, 16)
    newcont = ''
    start = 2
    offset = temp + 2
    newcont = ''
    while (readbytes > 0):
        newcont += content[offset:readbytes + offset]
        offset += readbytes
        endtemp = content.find('\r\n', offset + 2)
        readbytes -= 2
        if (endtemp > -1):
            strtemp = content[offset + 2:endtemp]
            readbytes = int(strtemp, 16)
            if (readbytes == 0):
                break
            else:
                offset = endtemp + 2
                readbytes-=2
    content = newcont
    return content

def download(id_all):
    if not os.path.exists('aicai'):
        os.mkdir('aicai')
    it=iter(range(1,15))
    for id  in id_all.keys():
        result = requests.get(url_download+id, headers=header,stream=True)
        #print(result.headers)
        filename=str(next(it))+'.xls'
        with open('./aicai/'+filename,'wb+') as f:
            f.write(result.content)
url_collect= 'https://live.aicai.com/pages/bf/sfc.shtml'
url_download='https://live.aicai.com/bf/bfindex!export.htm?matchBFId='

result=requests.get(url_collect,headers=header)
soup=BeautifulSoup(result.text,'html.parser')
all_url=soup.find_all('div',{'class':'bf_ta_tit'})
all_url2=[]
for ii in all_url:
    all_url2.append(ii.find('a')['value'])
all_url=all_url2
id_all={}
#print(all_url)
for x in all_url:
    x=str(x)
    a,b=x.split('=')[2:4]
    a=a.split('&')[0]
    b=b.split('&')[0]
    id_all[x[39:47]]=(a,b)

download(id_all)
print('ok!')

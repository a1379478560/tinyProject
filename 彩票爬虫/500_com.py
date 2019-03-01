import requests
from bs4 import BeautifulSoup
import os
import xlwt
import xlrd
download_url = r'http://odds.500.com/fenxi/europe_xls.php'
all_url=r'http://trade.500.com/sfc/'
header = {
    'User-Agent': r'Agent:Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.104 Safari/537.36 Core/1.53.4843.400 QQBrowser/9.7.13021.400' ,
    'Upgrade-Insecure-Requests': '1' ,
    'Referer': r'http://odds.500.com/fenxi/ouzhi-726453.shtml',
    'Pragma': 'no-cache',
    'Origin': r'http://odds.500.com',
    'Host': r'odds.500.com',
    'Content-Type': 'application/x-www-form-urlencoded',
    'Accept-Encoding':'gzip, deflate',
    'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
}
header2={
'User-Agent': r'Agent:Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.104 Safari/537.36 Core/1.53.4843.400 QQBrowser/9.7.13021.400' ,
}
scores={
    'fixtureid': '726453',
    'excelst': '1',
    'style': '0',
    'ctype': '1',
    'dcid': '',
    'scid': '',
    'r': '1',

}
# result=requests.post(download_url,headers=header,data=data)
# print(result.status_code)
# with open("1.xls",'wb+') as f:
#     f.write(result.content)
# result.encoding=result.apparent_encoding
# print(result.text)

def procxls():
    for ii in range(1,15):
        wb=xlrd.open_workbook(r'500_com/'+str(ii)+'.xls')
        sheet_read=wb.sheet_by_index(1)
        wbk=xlwt.Workbook(encoding='ascii')
        sheet_write=wbk.add_sheet('sheet1')
        for raws in range(6,sheet_read.nrows):
            for cols in range(sheet_read.ncols):
                sheet_write.write(raws-6,cols,sheet_read.cell(raws,cols).value)
        os.remove(r'500_com/'+str(ii)+'.xls')
        wbk.save(r'500_com/'+str(ii)+'.xls')

def getid(url):
    id=[]
    result=requests.get(url,headers=header2)
    #print('2',result.status_code)
    soup=BeautifulSoup(result.text,'html.parser')
    tr=soup.find_all('tr',{'data-vs': True})
    for x in tr:
        a=x.find_all('a',{'target': '_blank'})[3]
        id.append(a['href'][-12:-6])
    return id

def getxls(all_id):
    it = iter(range(1, 15))
    if not os.path.exists('500_com'):
        print("本目录下未找到500_com文件夹，已自动创建！")
        os.mkdir('500_com')
    for url_id in all_id:
        header['Referer']=r'http://odds.500.com/fenxi/ouzhi-'+url_id+'shtml'
        scores['fixtureid']=url_id
        result = requests.post(download_url, headers=header, data=scores)
        with open('500_com/'+str(next(it))+".xls", 'wb+') as f:
            f.write(result.content)

if __name__=='__main__':
    
    print('程序正在运行...')
    all_id=getid(all_url)
    print('已找到所有下载地址！')
    getxls(all_id)
    print("已经将14个xls文件全部下载完成")
    procxls()


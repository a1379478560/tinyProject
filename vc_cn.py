#coding=utf-8
#python version：2.7
#author:gouwh
#date:2018-05-06 11:47

import xlwt
import requests
from bs4 import BeautifulSoup
headers={
'User-Agent': r'Agent:Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.104 Safari/537.36 Core/1.53.4843.400 QQBrowser/9.7.13021.400',
}

def set_style(name, height, bold=False):
    style = xlwt.XFStyle()  # 初始化样式
    font = xlwt.Font()  # 为样式创建字体
    font.name = name
    font.bold = bold
    font.color_index = 4
    font.height = height
    style.font = font
    return style



def getContent(url,world,page):
    data=[]
    params={
        'q':word,
        'page':page,
    }
    r=requests.get(url,headers=headers,params=params)
    text=r.text.split('=',1)[-1]
    text=text.replace('<em>','')
    text=text.replace('</em>','')
    soup=BeautifulSoup(text,'html.parser')
    companys=soup.find_all('div',{'class':'company'})
    for com in companys:
        #print(com)
        name=com.find('a')['title']
        temp=com.find_all('a',{'data-remote':'true'})
        addr=temp[0].text
        try:
            tag=temp[1].text+'-'+temp[2].text
        except:
            tag=temp[1].text
        li=com.find_all('li')[-1]
        info=li.find('span').text.split('：')[-1]
        item=(name,addr,tag,info)
        data.append(item)
    print('第%s页完成！'% page)
    return data
def write(datalist):
    # 创建一个workbook 设置编码
    book = xlwt.Workbook(encoding='utf-8', style_compression=0)
    # 创建一个worksheet
    sheet = book.add_sheet(u'鲸准关键词搜索结果', cell_overwrite_ok=True)
    # 写入excel
    # 参数对应 行, 列, 值
    col = ['名称', '地址','标签','基本信息']
    sheet.write(0, 0, col[0], set_style('Times New Roman', 220, True))  # 插入表头并使用样式加黑
    sheet.write(0, 1, col[1], set_style('Times New Roman', 220, True))  # 插入表头并使用样式加黑
    sheet.write(0, 2, col[2], set_style('Times New Roman', 220, True))  # 插入表头并使用样式加黑
    sheet.write(0, 3, col[3], set_style('Times New Roman', 220, True))  # 插入表头并使用样式加黑
    for i in range(1,len(datalist)+1):
        item = datalist[i-1]
        for j in range(4):
            sheet.write(i, j, item[j])  # 数据
    book.save('result.xls')  # 保存

if __name__ == '__main__':
    scores=[]
    baseUrl = 'https://www.vc.cn/search/companies'
    word = input('输入搜索关键词\n')  # 搜索关键词
    page=input('要抓取的页数\n')
    for i in range(1,int(page)+1):
        scores= scores + getContent(baseUrl, word, i)

    write(scores)


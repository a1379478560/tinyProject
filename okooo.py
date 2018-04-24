import requests
from bs4 import BeautifulSoup
url='https://live.aicai.com/pages/bf/sfc.shtml'
header = {
    'User-Agent':'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6'
}
result=requests.get(url,headers=header)
soup=BeautifulSoup(result.text,'lxml')
all_url=soup.find_all('div',{'class':'bf_ta_tit'})
print(all_url)


# for item in soup.select('#gallery-list'):
#     for img in item.find_all('img'):
#         print('img',img)
#         img_path=img.get('m')
#         picaddr.append(img_path)
# for i,v in enumerate(picaddr):
#     # 将获取的v值再次放入request中进行与网站相应
#     image = requests.get(v)
#     # 存取图片过程中，出现不能存储 int 类型，故而，我们对他进行类型转换 str()。w:读写方式打开，b：二进制进行读写。图片一般用到的都是二进制。
#     with open('D:\\a\\img'+str(i)+'.jpg', 'wb') as file:
#         # content：图片转换成二进制，进行保存。
#         file.write(image.content)
#     print(i)

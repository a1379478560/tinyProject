a="[[1453250, 423, -1, '2017-11-25 08:00', 12284, 5109, '0-2', '0-0', '17', '11', 0.25, 0, '2', '0.5/1', 1, 1, 1, 1, 0, 0, '', '17', '11'], [1453249, 423, -1, '2017-11-25 08:30', 6145, 5112, '2-0', '1-0', '22', '23', 0.25, 0, '2', '0.5/1', 1, 1, 1, 1, 0, 1, '', '22', '23'], [1453247, 423, -1, '2017-11-26 04:05', 294, 730, '0-2', '0-1', '9', '5', 0.25, 0.25, '2', '0.5/1', 1, 1, 1, 1, 0, 0, '', '9', '5'], [1453254, 423, -1, '2017-11-26 06:00', 2609, 20733, '3-0', '1-0', '6', '2', 0.5, 0.25, '2', '0.5/1', 1, 1, 1, 1, 1, 2, '', '6', '2'], [1453257, 423, -1, '2017-11-26 08:35', 8490, 17584, '2-0', '0-0', '20', '4', 0, 0, '2', '0.5/1', 1, 1, 1, 1, 0, 0, '', '20', '4'], [1453255, 423, -1, '2017-11-27 04:00', 8308, 20740, '1-1', '0-1', '13', '18', 0.5, 0.25, '2', '0.5/1', 1, 1, 1, 1, 0, 0, '', '13', '18'], [1453248, 423, -1, '2017-11-27 04:00', 11009, 731, '2-0', '2-0', '25', '12', 0.25, 0, '1.5/2', '0.5/1', 1, 1, 1, 1, 0, 0, '', '25', '12'], [1453252, 423, -1, '2017-11-27 04:00', 2679, 14165, '3-1', '3-1', '16', '11', 0.5, 0.25, '1.5/2', '0.5/1', 1, 1, 1, 1, 1, 0, '', '16', '11'], [1453253, 423, -1, '2017-11-27 04:00', 5106, 13325, '1-0', '1-0', '9', '8', 0.25, 0, '2', '0.5/1', 1, 1, 1, 1, 0, 0, '', '9', '8'], [1453246, 423, -1, '2017-11-27 07:15', 18032, 4466, '2-1', '1-0', '5', '15', 0.25, 0.25, '2', '0.5/1', 1, 1, 1, 1, 1, 1, '', '5', '15'], [1453256, 423, -1, '2017-11-27 08:00', 20768, 13280, '2-1', '1-1', '20', '24', 0.25, 0.25, '1.5/2', '0.5/1', 1, 1, 1, 1, 0, 0, '', '20', '24'], [1453251, 423, -1, '2017-11-28 08:05', 12285, 20755, '2-1', '2-1', '22', '1', 0, 0, '2', '0.5/1', 1, 1, 1, 1, 0, 0, '', '22', '1']]"

import requests
header={
        'User-Agent': r'Agent:Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.104 Safari/537.36 Core/1.53.4843.400 QQBrowser/9.7.13021.400' ,
        }
# r=requests.get(url="http://info.310win.com/cn/CupMatch/90.html",headers=header)
# print(r.text)
def get_xls(self, uri):
    url = 'http://www.310win.com/1x2/' + uri + '.html'
    browser = webdriver.PhantomJS()  # 需要已将phantomjs.exe放入python的Scripts文件夹下
    # browser = webdriver.Chrome(r'E:/chromedriver.exe')
    browser.get(url)
    curent_page = browser.current_window_handle
    browser.find_element_by_xpath('//input[@name="chkall"]').click()  # click
    browser.find_element_by_xpath('//a[@onclick="exChange();return false;"]').click()

from selenium import webdriver
import time
url="http://info.310win.com/cn/SubLeague/2018-2019/37_90.html"
browser = webdriver.PhantomJS()  # 需要已将phantomjs.exe放入python的Scripts文件夹下
# browser = webdriver.Chrome(r'E:/chromedriver.exe')
browser.get(url)
time.sleep(5)
print(browser.page_source)
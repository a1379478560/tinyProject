from selenium import webdriver
import time
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
dcap = dict(DesiredCapabilities.PHANTOMJS)
dcap["phantomjs.page.settings.userAgent"] = (
    "Mozilla/5.0 (Linux; Android 5.1; OPPO R9tm Build/LMY47I; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043220 Safari/537.36 MicroMessenger/6.5.7.1041 NetType/4G Language/zh_CN",
)

for i in range(100000):
    try:
        url='http://7zsayl.v.vote8.cn/m?from=timeline'

        option = webdriver.ChromeOptions()
        option.add_argument('headless')
        browser=webdriver.Chrome('./chromedriver.exe',chrome_options=option)

        #browser = webdriver.Chrome('./chromedriver.exe')

        #browser = webdriver.PhantomJS(executable_path='./phantomjs.exe', desired_capabilities=dcap)   #需要已将phantomjs.exe放入python的Scripts文件夹下

        browser.set_page_load_timeout(50)
        browser.set_script_timeout(50)
        try:
            browser.get(url)
            time.sleep(2)
        except :
            browser.execute_script('window.stop()')
        page1=browser.find_element_by_xpath('//input[@id="option_7307033"]')  # click

        browser.execute_script("arguments[0].scrollIntoView(false);", page1)
        browser.execute_script("window.scrollBy(0, 200)")
        time.sleep(1.5)
        page1.click()
        page2=browser.find_element_by_xpath('//div[@class="Vote8ClickButton Vote8ClickButtonNormal"]')
        browser.execute_script("arguments[0].scrollIntoView();", page2)
        #browser.execute_script("window.scrollBy(0, 300)")
        time.sleep(1.5)
        page2.click()

        time.sleep(2)
        browser.find_element_by_xpath('//a[@class="btn btn-primary btn-lg btn-block"]').click()
        time.sleep(1)
        browser.get_screenshot_as_file('1.png')
        time.sleep(2)
        browser.get_screenshot_as_file('2.png')
        print('已投',i+1,'票')

    except :
        print('失败')
    finally:
        browser.close()

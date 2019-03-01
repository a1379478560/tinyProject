import os
from selenium.webdriver.common.keys import Keys
import time
from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait

curdir=os.path.abspath(os.curdir)
fileName="Bia I.doc"

def translate(fileName=fileName):
    if not  fileName.endswith(".doc"):
        return
    if "$" in fileName:
        return
    if "翻译结果" in fileName:
        return
    curdir=os.path.split(fileName)[0]
    #fileNameAbs=os.path.join(curdir,fileName)
    fileNameAbs=fileName
    downloadName=fileName[0:-4]+".vi.zh-CN.doc"

    now = int(time.time())
    timeStruct = time.localtime(now)
    strTime = time.strftime("%Y-%m-%d-%H-%M-%S", timeStruct)
    resultName=fileName[0:-4]+"-翻译结果"+strTime+".doc"  #暂时废弃，看下面
    resultName=os.path.join(curdir,"翻译结果-"+os.path.split(fileName)[1])

    if os.path.exists(os.path.join(curdir,resultName)):
        print("have translate")
        return
    host="www.onlinedoctranslator.com"

    options = webdriver.ChromeOptions()
    prefs = {'profile.default_content_settings.popups': 0, 'download.default_directory': curdir}
    options.add_experimental_option('prefs', prefs)

    options.add_argument('--disable-gpu')
    options.add_argument('--hide-scrollbars')
    options.add_argument('blink-settings=imagesEnabled=false')
    #options.add_argument('--headless')

    browser = webdriver.Chrome("chromedriver.exe",chrome_options=options)
    enable_download_in_headless_chrome(browser,curdir)
    browser.get("https://"+host+"/translationform")
    #print(browser.page_source)
    a=browser.find_element_by_xpath('//input[@type="file"]')
    a.send_keys(fileNameAbs)
    #time.sleep(3)
    alert=browser.switch_to_alert()
    alert.accept()

    selector_from = Select(browser.find_element_by_id("from"))
    selector_from.select_by_value("vi")
    selector_to = Select(browser.find_element_by_id("to"))
    selector_to.select_by_value("zh-CN")
    time.sleep(1)
    translate_button=browser.find_element_by_xpath('//input[@id="translation-button"]')

    while True:
        if translate_button.is_enabled():
            translate_button.click()
            break

    print("正在翻译...")
    while True:
        time.sleep(1)
        if os.path.exists(downloadName):
            os.rename(downloadName,resultName)
            browser.close()
            time.sleep(2)
            break
    print("翻译完成！")
def enable_download_in_headless_chrome( driver, download_dir):
    driver.command_executor._commands["send_command"] = ("POST", '/session/$sessionId/chromium/send_command')

    params = {'cmd': 'Page.setDownloadBehavior', 'params': {'behavior': 'allow', 'downloadPath': download_dir}}
    command_result = driver.execute("send_command", params)

def trans_dir(dir_path):
    file_list = os.listdir(dir_path)
    print(dir_path)
    print(file_list)
    for x in file_list:
        tempPath=os.path.join(dir_path,x)
        if os.path.isfile(tempPath):
            print("file")
            translate(fileName=tempPath)

        if os.path.isdir(tempPath):
            print("dir")
            trans_dir(tempPath)


if __name__ == '__main__':
    # while True:
    #     fileNameInput=input("请输入要翻译的文件名，直接回车默认"+fileName)
    #     if fileNameInput=="":
    #         fileNameInput=fileName
    #
    #     if not os.path.exists(fileNameInput):
    #         print("当前目录下未发现",fileNameInput)
    #         continue
    #     if  fileNameInput[-4:]==".doc":
    #         break
    #     else:
    #         print("请输入.doc文件")
    #
    # translate(fileName=fileNameInput)
    trans_dir(os.path.join(curdir,"raw"))

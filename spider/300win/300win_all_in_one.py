import requests
import re
import os
import time
import xlwt
from  bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.support.ui import Select
import warnings
warnings.filterwarnings("ignore")

class win310():
    def __init__(self):
        self.browser=webdriver.PhantomJS()
        self.header={
        'User-Agent': r'Agent:Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.104 Safari/537.36 Core/1.53.4843.400 QQBrowser/9.7.13021.400' ,
        }
        self.host="http://info.310win.com"
        #self.dazhou=-1
        self.guojia=-1
        self.saishi=-1
        self.year=-1
        self.match_id=-1
        self.year_list=[]
        self.subLeague_list=[]
        self.match_url_doc= ""
        self.match_url_js=""
        self.lx2ID_list=[]
        self.saishi_name=""
        self.wait_retry=[]
    def chose_page(self):
        # TODO 重新写一下这块的逻辑吧，按照js的来
        arrArea=[]
        url=r"http://info.310win.com/jsData/leftData/leftData.js"
        r=requests.get(url,headers=self.header)
        #print(r.text)
        pattern=re.compile(r"[[][[]'.*[]];")
        area_list=pattern.findall(r.text)
        for i in area_list:
            i=i.replace(";","")
            arrArea.append(eval(i))
        for i,x in enumerate(arrArea):
            print("{}. {}".format(i,x[0][0]))
        self.dazhou=int(input("请选择："))
        tmp=arrArea[int(self.dazhou)]
        for i,x in enumerate(tmp):
            print("{}. {}".format(i,x[0]))
        self.guojia = input("请选择：")
        tmp=tmp[int(self.guojia)][4:]
        #print(tmp)
        for i,xx in enumerate(tmp):
            for j,x in enumerate(xx):
                print("{} {}. {}".format(i,j,x[1]))
        n,m = input("输入两个数，空格隔开，请选择：").split(" ")
        self.saishi=(int(n),int(m))
        self.saishi_name=tmp[int(n)][int(m)][1]
        match_list=tmp[self.saishi[0]][self.saishi[1]]
        self.match_id=match_list[0] #实际的比赛id
        if self.saishi[0]==0:
            #print(match_list)
            match_url="/cn/"+("SubLeague" if match_list[4]==0 else "League") +"/"+str(self.match_id)+".html"
        else:
            match_url="/cn/CupMatch/"+str(self.match_id)+".html"
        self.match_url_doc=match_url
        return match_url

    def get_year_list(self):
        if self.match_id==-1:
            return 0
        url="http://info.310win.com/jsData/LeagueSeason/sea{}.js".format(self.match_id)
        r=requests.get(url=url,headers=self.header)
        pattern=re.compile(r"[[].*[]]")
        self.year_list=eval(pattern.findall(r.text)[0])
        return self.year_list

    def chose_year(self,url):
        if len(self.year_list)==0:
            self.get_year_list()
        for i,x in enumerate(self.year_list):
            print("{}. {}".format(i,x))
        n=int(input("输入年份编号："))
        self.year=self.year_list[n]
        pattern1=re.compile(r"/\d\d\d\d-\d\d\d\d/")
        pattern2=re.compile(r"/\d\d\d\d/")
        p1=pattern1.findall(url)
        p2=pattern2.findall(url)
        _year=p1 or p2
        self.match_url_doc=self.match_url_doc.replace("/" + str(self.match_id) + ".html", '/' + self.year + "/" + str(self.match_id) + ".html")
        r=requests.get(url=self.host+self.match_url_doc, headers=self.header)
        pattern=re.compile(r'/jsData/.*.js\?version=\d+')
        match_class_url=pattern.findall(r.text)
        url="http://info.310win.com"+match_class_url[0]
        self.match_url_js=url
        return url

    def get_match(self,match_url):
        r=requests.get(url="http://info.310win.com{}".format(match_url), headers=self.header)
        # print(r.text)
        # print(r.url)
        pattern=re.compile(r'/jsData/.*.js\?version=\d+')
        match_class_url=pattern.findall(r.text)
        url="http://info.310win.com"+match_class_url[0]
        url=self.chose_year(url)
        r=requests.get(url=url,headers=self.header)
        #print(r.url)
        # print(r.text)
        pattern_arrSubLeague=re.compile(r'arrSubLeague\s=\s[[][[].*;')
        arrSubLeague=pattern_arrSubLeague.findall(r.text)
        lx2ID_list=[]
        if len(arrSubLeague)>0:
            arrSubLeague=arrSubLeague[0].replace("arrSubLeague = ","").replace(";","")
            arrSubLeague=eval(arrSubLeague)
            arrSubLeague_num_list=list(map(lambda x:x[0],arrSubLeague))
            self.subLeague_list=arrSubLeague_num_list
            for subleague in self.subLeague_list:
                url=re.sub(r"_\d+\.js",'_'+str(subleague)+'.js',self.match_url_js)
                lx2ID_list+=self.url_to_lx2ID(url)
        else:
            lx2ID_list+=self.url_to_lx2ID(self.match_url_js)
        self.lx2ID_list=lx2ID_list
        return lx2ID_list
    def url_to_lx2ID(self,url):
        lx2_list=[]
        ret_lx2_list=[]
        #print(url)
        r=requests.get(url=url,headers=self.header)
        pattern=re.compile(r'jh[[]"[G|R].*[]][]];')
        pattern_arrTeam=re.compile(r"arrTeam\s=\s.*;")
        l2xId_raw=pattern.findall(r.text)
        arrTeam=pattern_arrTeam.findall(r.text)[0]
        arrTeam=arrTeam.replace("arrTeam = ","")
        arrTeam=arrTeam.replace(";","")
        arrTeam=eval(arrTeam)
        #print(l2xId_raw[8])
        # print(len(l2xId_raw))
        # print(l2xId_raw)
        for i,x in enumerate(l2xId_raw):
            x_t=x.replace(";","")
            tmp=re.sub(r'jh[[].*[]]\s=\s',"",x_t)
            tmp=tmp.replace(",,",",0,").replace(",,",",0,").replace(",,",",0,").replace(",,",",0,").replace(",,",",0,").replace(",,",",0,").replace(",,",",0,")
            #print(i,tmp)
            tmp=re.sub(r'<a.*?</a>'," ",tmp)
            lx2_list+=eval(tmp)
            # print(tmp)
            # print(eval(tmp))
        for raw in lx2_list:
            try:
                lx2=raw[0]
                match_time=raw[3]
                team1_id=raw[4]
                team2_id=raw[5]
                team1=self.team_id_to_name(team1_id,arrTeam)
                team2=self.team_id_to_name(team2_id,arrTeam)
                score=raw[6].replace("取消|取消|Cancel","取消").replace("|","_")
                ret_lx2_list.append((lx2,match_time,team1,team2,score))
            except:    #处理附加赛
                for x in raw:
                    if type(x)==list:
                        lx2 = x[0]
                        match_time = x[3]
                        team1_id = x[4]
                        team2_id = x[5]
                        team1 = self.team_id_to_name(team1_id, arrTeam)
                        team2 = self.team_id_to_name(team2_id, arrTeam)
                        score = x[6].replace("取消|取消|Cancel","取消").replace("|","_")
                        ret_lx2_list.append((lx2, match_time, team1, team2, score))
        return ret_lx2_list
    def team_id_to_name(self,team_id,arrTeam):
        for x in arrTeam:
            if x[0]==team_id:
                return x[1]
        return -1

    def get_xls(self,l2x_tuple):
        if "延后" in l2x_tuple[4] or "推迟" in l2x_tuple[4] or "取消" in l2x_tuple[4]:
            return
        if l2x_tuple[4]=="":
            return
        url='http://www.310win.com/1x2/'+str(l2x_tuple[0])+'.html'
        browser = webdriver.PhantomJS() #需要已将phantomjs.exe放入python的Scripts文件夹下
        #browser = webdriver.Chrome(r'E:/chromedriver.exe')
        browser.get(url)
        curent_page = browser.current_window_handle
        Select(browser.find_element_by_id("sel_showType")).select_by_value("1")
        Select(browser.find_element_by_id("sel_showType")).select_by_value("2")
        time.sleep(1)
        browser.find_element_by_xpath('//input[@name="chkall"]').click()  # click
        browser.find_element_by_xpath('//a[@onclick="exChange();return false;"]').click()
        handles = browser.window_handles

        for handle in handles:  # 切换窗口
            if handle != browser.current_window_handle:
                #print('switch to ', handle)
                browser.switch_to_window(handle)
                #print(browser.current_window_handle)  # 输出当前窗口句柄
                break
        result_url=browser.current_url
        #time.sleep(5)
        # for handle in handles:
        #         browser.switch_to_window(handle)
        #         browser.close()
        xls_url=result_url+"&print=true"
        #print(xls_url)
        if not os.path.exists(self.saishi_name):
            os.mkdir(self.saishi_name)
        file_name=self.saishi_name+"/"+l2x_tuple[1]+"+"+l2x_tuple[2]+"+"+l2x_tuple[4]+"+"+l2x_tuple[3]+".xls"
        file_name=file_name.replace(" ","_").replace(":","：")
        if "html&print=true" in xls_url:
            print("本场无比赛记录："+file_name)

            return
        with open(file_name,"w",encoding="gbk") as fp:
            r=requests.get(xls_url,headers=self.header)
            # print(r.apparent_encoding)
            # print(r.encoding)
            # print(xls_url)
            r.encoding="gbk"
            fp.write(r.text)
        print("爬取文件："+file_name)

win=win310()
match_url=win.chose_page()
match=win.get_match(match_url)

for m in match:
    try:
        win.get_xls(m)
    except:
        print("爬取失败，等待重试：",m,)
        win.wait_retry.append([m,3])
    time.sleep(1)
print("开始重抓取失败数据。。。")

while win.wait_retry:
    retry=win.wait_retry.pop(0)
    if retry[1]<=0:
        print("超过最大重试次数!!!!!!：",retry[0])
        continue
    try:
        win.get_xls(retry[0])
    except:
        retry[1]-=1
        win.wait_retry.append(retry)

print("爬取完成！")
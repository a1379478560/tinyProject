import requests
import re
import time
# base_url="http://domain.aliyuncs.com/"
# params={
#     "Action":"CheckDomain",
#     "DomainName":"abc.com",
#     "Version":"2016-05-11",
#     "Format":'JSON',
#     "AccessKeyId":"LTAIFRoXQQXa1Pnq",
#     ""
# }
# r=requests.get(url=base_url+"12.com")
# print(r.text)
base_url="http://panda.www.net.cn/cgi-bin/check.cgi?area_domain="
patrtern=re.compile("<original>210")

base_url1="http://pandavip.www.net.cn/check/check_ac1.cgi?domain="
patrtern1=re.compile("210")

base_url2="https://cnz.co/domain-registration/domain.php?action=caajax&domain_name="
patrtern2=re.compile('"available"')

for i in range(19165,15616546):
    domain=str(i)+".com"
    domain1=str(i)+".cn"
    domain2=str(i)+".cc"

    r=requests.get(base_url+domain)
    r1=requests.get(base_url1+domain1)
    r2=requests.get(base_url2+domain2)

    if(patrtern.findall(r.text)):
        print(domain)
    if(patrtern1.findall(r1.text)):
        print(domain1)
    if(patrtern2.findall(r2.text)):
        print(domain2)
    time.sleep(1)
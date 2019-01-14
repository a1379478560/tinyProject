import requests
from bs4 import BeautifulSoup
import xlrd
import xlwt

def readxls(fileName="1.xls"):
    data=[]
    wb=xlrd.open_workbook(fileName)
    sheet=wb.sheet_by_index(0)
    rows=sheet.nrows
    for row in range(1,rows):
        d=sheet.row_values(row)

        if len(d)==1 :
            temp="0000"
        elif len(d[1])<5:
            temp="0000"
        else:
            temp=d[1]
        if type(d[0])==str and len(d[0])==17:
            data.append([d[0],temp])
        else:
            print("第",row+1,"行VIN码",d[0],"格式不对")
    return data

def getOne(session,vin):
    url="http://10.192.0.29/zccx/vinDecodingList.shtml?cn=y&pageno=1"
    header = {
        'User-Agent': r'Agent:Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.104 Safari/537.36 Core/1.53.4843.400 QQBrowser/9.7.13021.400',
        'Upgrade-Insecure-Requests': '1',
        'Referer': r'http://10.192.0.29/zccx/vinDecodingList.shtml?cn=y&pageno=1',

        'Origin': r'http://10.192.0.29',
        'Host': r'10.192.0.29',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Accept-Encoding': 'gzip, deflate',
        'Accept': "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
        'Accept-Language':'zh-CN,zh;q=0.9',
        'Cache-Control':'max-age=0',
        #'Cookie':'JSESSIONID=xybcqH_kOdf-96LToqXiGeC3unzSd3eGSxqQM_fyM7kMDuHCTsZL!1836396137',
    }
    params={
        'fvinRoot':vin,
        'newInterface':'0',
        'car_vinCode':vin,
        'qtype':'3',
        'requestSource':'http://10.192.0.36:80/flexitm/itm/product/result.jsp?vinflag=0',
    }
    try:
        r=session.post(url=url,headers=header,data=params)
        soup=BeautifulSoup(r.text,"html.parser")
        table=soup.find_all('table',{'id':'zhcx','border':'0','cellpadding':'0','align':'center'})[1]
        tr=table.find_all('tr')[1]
        td=tr.find_all('td',)[1]
        result=td.text.strip()
    except:
        print(vin,"未找到")
        result='未找到'

    # print(td)
    # print(len(td))
    return result

def getsession():
    session = requests.session()
    session.get(url='http://10.192.0.29/zccx/search?regionCode=00000000&businessNature=A&operatorCode=0000000000&returnUrl=http://10.192.0.36:80/flexitm/itm/product/result.jsp?vinflag=0#')
    return session

def getAllitem(data):
    session=getsession()
    for item in data:
        if item[1]=='0000':
            item[1]=getOne(session,item[0])
    return data

def writexls(newData,saveFileName='result.xls'):
    wbk=xlwt.Workbook(encoding='ascii')
    sheet=wbk.add_sheet('查询结果')
    for i,x in enumerate(newData):
        sheet.write(i,0,x[0])
        sheet.write(i,1,x[1])
    wbk.save(saveFileName)
    print("查询结果已经保存到",saveFileName)

#x=getOne(getsession(),'1LN6L9S98H5613768')
#print(x)
if __name__=='__main__':
    fileName=input("请输入文件名，默认1.xls")
    if fileName=='':
        data=readxls()
    else:
        data=readxls(fileName)
    print("共",len(data),"条有效记录")
    print("开始查询...")
    newData=getAllitem(data)
    print("查询完成，写入文件")
    writexls(newData)
    print("写入完成！")
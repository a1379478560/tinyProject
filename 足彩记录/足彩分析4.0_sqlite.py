import xlrd
from xlutils.copy import copy
import operator
import os
import sqlite3

dbName="result.db"
try:
    conn = sqlite3.connect(dbName)
    cursor = conn.cursor()
    print("连接数据库成功！")
except:
    print("链接数据库失败！")
    exit(-1)

def readxls_auto(fileName):
    data={}
    status=[]
    temp=[]
    #fileName="14场/亚盘分析"+id+".xls"
    wbk=xlrd.open_workbook(fileName)
    sheet_read=wbk.sheet_by_index(0)
    data["winner"]=sheet_read.cell_value(0,0)
    data["ballNum"]=sheet_read.cell_value(1,3)
    temp=sheet_read.row_values(1,0,7)
    temp.pop(3)
    status+=temp
    temp = sheet_read.row_values(2, 0, 7)
    temp.pop(3)
    status += temp
    temp = sheet_read.row_values(3, 0, 7)
    temp.pop(3)
    status += temp
    data["status"]=status
    data["result"]=sheet_read.cell_value(6,0)
    return data

def selectdb(data):
    table_dic={"盈亏":"yingkui","主胜":"zhusheng","平局":"pingju",}
    table=table_dic[data["winner"]]
    status="|".join(data["status"])
    ballNum=data["ballNum"]
    sql="select result from {} where status=? and ballNum=? ".format(table)
    res=cursor.execute(sql,(status,ballNum))
    res=list(res)
    if len(res):
        return list(map(lambda x:x[0],res))
    return False

def insertdb(data):
    table_dic={"盈亏":"yingkui","主胜":"zhusheng","平局":"pingju",}
    table=table_dic[data["winner"]]
    status="|".join(data["status"])
    ballNum=data["ballNum"]
    result=data["result"]
    sql="insert into {} (status,ballNum,result) values(?,?,?)".format(table)
    cursor.execute(sql, (status, ballNum,result))
    conn.commit()


def printres(data):
    print(data['winner'])
    for i in range(18):
        print(data['status'][i],end="  ")
        if (i+1)%6==0:
            print()
    print(data['ballNum'])




if __name__ == '__main__':
    path = "autoAnalyze"
    for fpathe, dirs, fs in os.walk(path):
        for f in fs:
            abspath=os.path.join(fpathe, f)
            data=readxls_auto(abspath)
            flag = selectdb(data)
            if flag:
                res_list = flag[0]
                if data["result"] not in res_list:
                    insertdb(data)
            else:
                insertdb(data)



conn.close()
import xlrd
from xlutils.copy import copy
import operator
import sqlite3

dbName="result.db"
try:
    conn = sqlite3.connect(dbName)
    cursor = conn.cursor()
    print("连接数据库成功！")
except:
    print("链接数据库失败！")
    exit(-1)

def readxls(fileName):
    data={}
    status=[]
    temp=[]
    fileName="autoAnalyze/亚盘分析"+fileName+".xls"
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
        ret=list(map(lambda x: x[0], res))
        ret=list(set(ret))
        return ret
    return False

def insertdb(data,res):
    table_dic={"盈亏":"yingkui","主胜":"zhusheng","平局":"pingju",}
    table=table_dic[data["winner"]]
    status="|".join(data["status"])
    ballNum=data["ballNum"]
    result=res
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
    while True:
        id=input("请输入数字\n")
        if  not id.isdigit():
            print("输入有误，请输入数字！")
            continue

        data=readxls(id)
        # print(len(data["status"]))
        printres(data)
        flag=selectdb(data)
        if flag:
            print(flag)
        else:
            res=input("这场重点分析，请输入分析结果：\n")
            insertdb(data,res)
        print("本次查询结束，查询下一个请继续输入数字，否则直接关闭程序！")
        print("*************************************************************")

conn.close()
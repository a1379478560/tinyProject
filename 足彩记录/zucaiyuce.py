import xlrd
from xlutils.copy import copy
import operator

dbName="db.xls"

def readxls(id):
    data={}
    status=[]
    temp=[]
    fileName="14场/三套总表"+id+".xls"
    wbk=xlrd.open_workbook(fileName)
    sheet_read=wbk.sheet_by_index(0)
    data["winner"]=sheet_read.cell_value(0,0)
    data["ballNum"]=sheet_read.cell_value(1,3)
    temp=sheet_read.row_values(1,0,9)
    temp.pop(3)
    status+=temp
    temp = sheet_read.row_values(2, 0, 9)
    temp.pop(3)
    status += temp
    temp = sheet_read.row_values(3, 0, 9)
    temp.pop(3)
    status += temp
    data["status"]=status
    return data

def selectdb(data):
    wbk=xlrd.open_workbook(dbName)
    sheet=wbk.sheet_by_name(data['winner'])
    nrows=sheet.nrows

    for i in range(nrows):
        line=sheet.row_values(i,0,24)
        if operator.eq(line,data["status"]) and data['ballNum']==sheet.cell_value(i,24):
            return sheet.cell_value(i,25)
    return False

def writexls(data,res):
    rbk=xlrd.open_workbook(dbName)
    sheet=rbk.sheet_by_name(data['winner'])
    nrows = sheet.nrows
    wbk=copy(rbk)
    sheet_w=wbk.get_sheet(data['winner'])
    for i in range(24):
        sheet_w.write(nrows,i,data['status'][i])
    sheet_w.write(nrows,24,data['ballNum'])
    sheet_w.write(nrows,25,res)
    wbk.save(dbName)

def printres(data):
    print(data['winner'])
    for i in range(24):
        print(data['status'][i],end="  ")
        if (i+1)%8==0:
            print()
    print(data['ballNum'])

if __name__ == '__main__':
    while True:
        id=input("请输入数字\n")
        if  not id.isdigit():
            print("输入有误，请输入数字！")
            continue

        data=readxls(id)
        #print(data['status'])
        printres(data)
        flag=selectdb(data)
        if flag:
            print(flag)
        else:
            res=input("这场重点分析，请输入分析结果：\n")
            writexls(data,res)
        print("本次查询结束，查询下一个请继续输入数字，否则直接关闭程序！")
        print("*************************************************************")

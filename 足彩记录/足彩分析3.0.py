import xlrd
from xlutils.copy import copy
import operator
import os

dbName="db-jzbz.xls"

def readxls(id):
    data={}
    status=[]
    temp=[]
    fileName="14场/亚盘分析"+id+".xls"
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
    wbk=xlrd.open_workbook(dbName)
    sheet=wbk.sheet_by_name(data['winner'])
    nrows=sheet.nrows

    for i in range(nrows):
        line=sheet.row_values(i,0,18)
        if operator.eq(line,data["status"]) and data['ballNum']==sheet.cell_value(i,18):
            res_list=[]
            j=19     #第19个单元格开始存储分析结果
            while True:
                if sheet.cell_value(i,j)=="END":
                    break
                else:
                    res_list.append(sheet.cell_value(i,j))
                    j+=1
            return res_list,i
    return False

def writexls(data,res):
    rbk=xlrd.open_workbook(dbName)
    sheet=rbk.sheet_by_name(data['winner'])
    nrows = sheet.nrows
    wbk=copy(rbk)
    sheet_w=wbk.get_sheet(data['winner'])
    selectdbdata=selectdb(data)
    if selectdbdata:
        write_col=19
        for res_item in res:
            sheet_w.write(selectdbdata[1], write_col, res_item)
            write_col+=1
        sheet_w.write(selectdbdata[1], write_col, "END")
    else:
        for i in range(18):
            sheet_w.write(nrows,i,data['status'][i])
        sheet_w.write(nrows,18,data['ballNum'])
        sheet_w.write(nrows,19,res[0])
        sheet_w.write(nrows, 20, "END")
    wbk.save(dbName)

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
                    res_list.append(data["result"])
                    writexls(data, res_list)
            else:
                writexls(data, [data["result"], ])
    # while True:
    #     id=input("请输入比赛场次>>>>：\n")
    #     if  not id.isdigit():
    #         print("输入有误，请输入数字！")
    #         continue
    #
    #     data=readxls(id)
    #     printres(data)
    #     flag=selectdb(data)
    #     if flag:
    #         print(flag[0])
    #         res=input("请输入新的分析结果，没有的话直接回车跳过：")
    #         if res!="":
    #             res_list=flag[0]
    #             res_list.append(res)
    #             writexls(data,res_list)
    #     else:
    #         res=input("这场重点分析，请输入分析结果：\n")
    #         writexls(data,[res,])
    #     print("本次↑↑查询结束，查询下一个请继续输入数字，否则直接关闭程序！")
    #     print("*************************************************************")


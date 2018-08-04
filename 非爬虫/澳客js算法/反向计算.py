import xlrd
import xlwt
import math
def readxls(fileName):
    data=[]
    wb=xlrd.open_workbook(fileName)
    sheet=wb.sheet_by_index(0)
    rows=sheet.nrows

    def toint(x):
        if(type(x)==type(" ")):
            x=float(x)
        return x

    for row in range(1,rows):
        d=sheet.row_values(row)
        for i in range(7):
            d[i]=toint(d[i])
        data.append(d)
    return data

def calOne(x):
    r = []
    A=(1-x[3]/100)/x[0]
    B=(1-x[4]/100)/x[1]
    C=(1-x[5]/100)/x[2]

    B=B/A
    C=C/A
    A=x[6]
    B=B*A
    C=C*A


    D=x[3]/100/(A+B+C)
    E=x[4]/100/(A+B+C)
    F=x[5]/100/(A+B+C)
    E=E/D
    F=F/D
    D=x[6]
    E=E*D
    F=F*D

    r.append(A)
    r.append(B)
    r.append(C)
    r.append(D)
    r.append(E)
    r.append(F)
    return r


'''
alls=wins+ties+defeats
win=alls-wins*winp
tie=alls-ties*tiep
defeat=alls-defeats*defeatp


(x+y+z)-ax=A(x+y+z)
(x+y+z)-by=B(x+y+z)
(x+y+z)-cz=C(x+y+z)

AA=x/(x+y+z)      x/(x+y+z)=(1-A)/a       0.1665         0.3333   0.5
BB=y/(x+y+z)                       29.36  46.67
CC=z/(x+y+z)
'''

def calAll(data):
    result=[]
    for x in data:
        result.append(calOne(x))
    return result
def writexls(fileName,data):
    wb=xlwt.Workbook()
    sheet=wb.add_sheet("sheet1")
    sheet.write(0, 0, "主盈亏")
    sheet.write(0, 1, "平盈亏")
    sheet.write(0, 2, "客盈亏")
    sheet.write(0, 3, "主指数")
    sheet.write(0, 4, "平指数")
    sheet.write(0, 5, "客指数")

    for i,x in enumerate(data):
        for j,y in enumerate(x) :
            sheet.write(i+1,j,y)

    wb.save(fileName)

if __name__=="__main__":
    scores=readxls("1.xlsx")
    result=calAll(scores)
    writexls("计算结果.xls",result)
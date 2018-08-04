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
        for i in range(6):
            d[i]=toint(d[i])
        data.append(d)
    return data

def calOne(x):
    r=[]
    wins=x[0]
    ties=x[1]
    defeats=x[2]

    winp=x[3]
    tiep=x[4]
    defeatp=x[5]

    alls=wins+ties+defeats

    win=alls-wins*winp
    tie=alls-ties*tiep
    defeat=alls-defeats*defeatp
    def round(x):
        return math.floor(x+0.5)
    r.append(round((win * 100) / 100))
    r.append(round((tie * 100) / 100))
    r.append(round((defeat * 100) / 100))
    r.append(round((win / alls) * 100))
    r.append(round((tie / alls) * 100))
    r.append(round((defeat / alls) * 100))
    return r


'''

alls=wins+ties+defeats
win=alls-wins*winp
tie=alls-ties*tiep
defeat=alls-defeats*defeatp


(x+y+z)-ax=A(x+y+z)
(x+y+z)-by=B(x+y+z)
(x+y+z)-cz=C(x+y+z)

AA=x/(x+y+z)      AA=(1-A)/a       0.1665         0.3333   0.5
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
    scores=readxls("1.bak.xlsx")
    result=calAll(scores)
    writexls("计算结果0.xls",result)
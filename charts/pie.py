from pyecharts import Pie
import xlrd

filename='2012毕设.xls'
scores = xlrd.open_workbook(filename)
sheet1=scores.sheet_by_index(0)
nrows = sheet1.nrows
source={}
for i in range(6,nrows):
    a=sheet1.cell_value(i,6)
    if a in source.keys():
        source[a]+=1
    else:
        source[a]=1
print(source)

value=[]
attr=[]
for k in source:
    kk=k.replace(' ','')
    if kk=='':
        continue
    attr.append(kk)
    value.append(source[k])
pie=Pie("题目来源",width=800, height=600)
pie.add("",attr,value,is_label_show=True)
pie.render()
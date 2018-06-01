from pyecharts import Pie
import xlrd

filename='2012毕设.xls'
data = xlrd.open_workbook(filename)
sheet1=data.sheet_by_index(0)
nrows = sheet1.nrows
source={}
value=[0,0,0]
attr=['工程实践','研究设计','理论分析']
for i in range(6,nrows):
    a = sheet1.cell_value(i, 7).replace(' ','')
    b = sheet1.cell_value(i, 8).replace(' ','')
    c = sheet1.cell_value(i, 9).replace(' ','')
    if a=='√':
        value[0]+=1
    if b=='√':
        value[1]+=1
    if c=='√':
        value[2]+=1
print(value)

pie=Pie("",width=800, height=600)
pie.add("",attr,value,radius=[45,75],is_label_show=True,label_text_color=None,legend_orient="vertical",legend_pos='left',tooltip_background_color='rgba(00,50,100,0.7)')


pie.show_config()
pie.render()
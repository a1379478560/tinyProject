from pyecharts import Geo,Map
import xlrd

filename='统计信息.xlsx'
data = xlrd.open_workbook(filename)
sheet1=data.sheet_by_index(0)
nrows = sheet1.nrows
city={}
for i in range(1,nrows):
    a=sheet1.cell_value(i,3)
    if a in city.keys():
        city[a]+=1
    else:
        city[a]=1
print(city)
value=[]
attr=[]
for k in city:
    kk=k.replace('省','')
    attr.append(kk)
    value.append(city[k])
map=Map("省份分布图", width=1200, height=600)
map.add("", attr, value, maptype='china', is_visualmap=True, is_label_show =True,visual_text_color='#F55',visual_range=(1,5))
map.show_config()
map.render()

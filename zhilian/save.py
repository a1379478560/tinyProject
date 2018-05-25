import os
import xlwt
import pymysql
def save_xls(path,filename,data):
    filename+='.xls'
    wbk = xlwt.Workbook(encoding='ascii')
    sheet1 = wbk.add_sheet('智联招聘数据')
    sheet1.write(0,0,'职位名称')
    sheet1.write(0, 1, '公司名称')
    sheet1.write(0, 2, '月薪')
    sheet1.write(0, 3, '上班地点')
    sheet1.write(0, 4, '反馈率')
    sheet1.write(0, 5, '更新时间')
    raw=1
    for x in data:
        sheet1.write(raw, 0, x[0])
        sheet1.write(raw, 1, x[1])
        sheet1.write(raw, 2, x[2])
        sheet1.write(raw, 3, x[3])
        sheet1.write(raw, 4, x[4])
        sheet1.write(raw, 5, x[5])
        raw+=1
    wbk.save( os.path.join(path,filename))
def save_text(path,filename,data):
    filename+='.txt'
    with open(os.path.join(path,filename),'w') as f:
        #row = '%-35s%-45s%-10s%-15s%-10s%-8s\n' % ('职位名称', '公司名称', '月薪', '上班地点', '反馈率', '更新时间')
        row='职位名称'.ljust(30)+'公司名称'.ljust(35)+'月薪'.ljust(8)+'上班地点'.ljust(10)+'反馈率'.ljust(5)+'更新时间'.ljust(5)+'\n'
        f.write(row)
        for x in data:
            row = x[0].ljust(30) + x[1].ljust(35) + x[2].ljust(8) + x[3].ljust(10) + x[4].ljust(5) + x[5].ljust(5)+'\n'
            #row = '%-35s%-45s%-10s%-15s%-10s%-8s\n' % (x[0], x[1], x[2],x[3],x[4],x[5])
            f.write(row)

def save_mysql():
    pass
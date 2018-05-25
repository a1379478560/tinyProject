
#mysql存储方式需要先执行下面 sql语句来创建数据库  或者直接导入本项目根目录的zhilian.sql


# CREATE DATABASE `zhilian` DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci;
# CREATE TABLE `zhilian_pos` (
#   `id` int(11) NOT NULL AUTO_INCREMENT,
#   `pos_name` char(128) DEFAULT NULL,
#   `com_name` char(128) DEFAULT NULL,
#   `fk_lv` char(16) DEFAULT NULL,
#   `salary` char(32) DEFAULT NULL,
#   `update_time` char(32) DEFAULT NULL,
#   `site` char(128) DEFAULT NULL,
#   PRIMARY KEY (`id`)
# ) ENGINE=InnoDB AUTO_INCREMENT=181 DEFAULT CHARSET=utf8;


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
# def connectdb(host,user,passwd,dbname):
#     try:
#         #db=pymysql.connect('140.143.143.164','ferris','123456','launcher')
#         db = pymysql.connect(host, user, passwd, dbname)
#         cursor=db.cursor()
#         print('数据库连接成功！')
#         cursor.execute('SELECT VERSION()')
#     except:
#         print('数据库连接失败，请检查')
#     return db

def save_mysql(host,user,passwd,dbname,data):
    try:
        db = pymysql.connect(host, user, passwd, dbname,use_unicode=True, charset="utf8")
        cursor=db.cursor()
        print('数据库连接成功！')
        cursor.execute('SELECT VERSION()')
    except:
        print('数据库连接失败，请检查')
        return  0
    cursor=db.cursor()
    print('正在插入数据！')
    for item in data:
        sql='INSERT INTO zhilian_pos(pos_name, com_name,salary,site,fk_lv,update_time) VALUES("%s", "%s","%s","%s","%s","%s");' %(item[0],item[1],item[2],item[3],item[4],item[5])
        try:
            cursor.execute(sql)
            db.commit()
        except pymysql.err.IntegrityError:
            print('重复数据')
            db.rollback()
        except:
            raise
            print('插入失败')
            db.rollback()

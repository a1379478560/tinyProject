from .save  import *
from .spider import *
from tkinter import *
from tkinter.filedialog import askdirectory
import threading
from tkinter import scrolledtext
import datetime,time
POSITION=[]        #保存抓到的数据
I=0                #已经爬取的页数
STATUS=1           #控制爬虫线程的工作与停止状态   0为停止 1为工作
path=r'C:/Users/sheldon/Desktop'           # 保存成Excel或txt文件时的路径和文件名
name='result'
def getalldata(city,kw,pages,start_page=1):
    addlog('开始爬取数据')
    global STATUS
    global POSITION
    global I
    #print(STATUS)
    for i in range(start_page,pages+1):

        if not STATUS:
            #print(STATUS)
            I=i-1
            addlog('暂停爬取数据，共爬了%s页数据' % (I))
            break
        addlog('开始第%s页...'%(i))
        position,pos_num=getonepagedata(city,kw,i)
        POSITION+=position
        addlog('ok')
        #print(pos_num)

        if i >=int(pos_num)//60+1:
            I=i
            break
    return POSITION,I  #i是实际爬取的页数，因为输入的页数可能大于实际有的页数

def addlog(str1):
    log=datetime.datetime.now().strftime('%H:%M:%S')+"  "+str1+'\n'
    t.insert(END,log)
def start():
    global STATUS,POSITION,I
    POSITION=[]
    I=0
    page=page_entry.get()
    city=city_entry.get()
    kw=kw_entry.get()
    if page=='' or city==''or page=='':
        addlog('城市，关键词，页码都不能为空！')
        return
    STATUS = 1
    t=threading.Thread(target=getalldata, args=(city,kw,int(page)))
    t.start()

def stop():
    global STATUS
    global I
    if STATUS==0:
        return
    STATUS=0

def restart():
    global STATUS,I
    if STATUS==1:
        return
    addlog('继续爬取数据')
    page=page_entry.get()
    city=city_entry.get()
    kw=kw_entry.get()
    STATUS = 1
    t=threading.Thread(target=getalldata, args=(city,kw,int(page),I+1))
    t.start()

def fun_select():
    global path
    path = askdirectory()
    lb_path['text']='保存路径：'+path

def savexls():
    addlog('正在保存为Excel文件')
    save_xls(path, file_entry.get(), POSITION)
    addlog('保存成功')
def savetxt():
    addlog('正在保存为TXT文件')
    save_text(path, file_entry.get(), POSITION)
    addlog('保存成功')
def savesql():
    addlog('正在保存到mysql')
    flag=save_mysql(host_entry.get().split(':')[0],user_entry.get(),pw_entry.get(),db_entry.get(),POSITION)
    if flag==0:
        addlog('数据库连接失败')
    else:
        addlog('正在插入数据')
        addlog('保存成功')
if __name__=='__main__':
    # pos_data,p=getalldata('北京','python',3)
    # print(p)
    # save_mysql('123.206.90.65','root','130129','zhilian',pos_data)

    root = Tk(className='智联招聘岗位')
    root.geometry('900x450')
    root.resizable(0,0)

    city_label = Label(root, text='爬取城市', anchor='w')
    city_label.place(x=20, y=30, width=320, height=20)
    city_entry=Entry(root)
    city_entry.insert(0,'北京')
    city_entry.place(x=80,y=30)

    kw_label = Label(root, text='关键词', anchor='w')
    kw_label.place(x=240, y=30, width=320, height=20)
    kw_entry=Entry(root)
    kw_entry.insert(0,'会计')
    kw_entry.place(x=300,y=30)

    page_label = Label(root, text='爬取页数', anchor='w')
    page_label.place(x=450, y=30, width=320, height=20)
    page_entry=Entry(root)
    page_entry.insert(0,'5')
    page_entry.place(x=520,y=30)

    btn_del = Button(root, text='开始', command=start)
    btn_del.place(x=50, y=80, height=45,width=150)

    btn_del = Button(root, text='暂停爬虫', command=stop)
    btn_del.place(x=270, y=80, height=45,width=150)

    btn_del = Button(root, text='重新开始', command=restart)
    btn_del.place(x=490, y=80, height=45,width=150)

    page_label = Label(root, text='保存数据', anchor='w')
    page_label.place(x=20, y=150, width=320, height=20)

    lb_path = Label(root, text='保存路径：' + path, anchor='w')
    lb_path.place(x=20, y=190, width=320, height=20)

    select_btn = Button(root, text='选择', command=fun_select)
    select_btn.place(x=300, y=180, width=50, height=30)

    filename_label = Label(root, text='文件名', anchor='w')
    filename_label.place(x=400, y=185, width=220, height=20)
    file_entry=Entry(root)
    file_entry.insert(0,name)
    file_entry.place(x=450,y=185)


    btn_del = Button(root, text='保存为Excel', command=savexls)
    btn_del.place(x=100, y=250, height=45,width=150)
    btn_del = Button(root, text='保存为TXT', command=savetxt)
    btn_del.place(x=350, y=250, height=45,width=150)

    host_label = Label(root, text='主机地址', anchor='w')
    host_label.place(x=20, y=320, width=220, height=20)
    host_entry=Entry(root)
    host_entry.insert(0,'123.206.90.65:3306')
    host_entry.place(x=100,y=320)

    user_label = Label(root, text='用户名', anchor='w')
    user_label.place(x=260, y=320, width=220, height=20)
    user_entry=Entry(root)
    user_entry.insert(0,'root')
    user_entry.place(x=320,y=320)

    pw_label = Label(root, text='密   码', anchor='w')
    pw_label.place(x=20, y=380, width=220, height=20)
    pw_entry=Entry(root)
    pw_entry.insert(0,'130129')
    pw_entry['show']='*'
    pw_entry.place(x=100,y=380)

    db_label = Label(root, text='数据库名', anchor='w')
    db_label.place(x=260, y=380, width=220, height=20)
    db_entry=Entry(root)
    db_entry.insert(0,'zhilian')
    db_entry.place(x=320,y=380)

    btn_del = Button(root, text='保存到mysql', command=savesql)
    btn_del.place(x=480, y=340, height=45,width=150)

    t = scrolledtext.ScrolledText(root,  background='#ffffff')
    t.place(x=680,y=30,width=200, height=400,)
    root.mainloop()
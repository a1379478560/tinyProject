from tkinter import *
from tkinter.filedialog import askdirectory
import os
import time
import threading
import shutil
import time
flag=0
src_file=r''
to_file=[]
file_list=[]
file_now=[]
def readini():

    try:
        with open('fd.ini','r') as f:
            global src_file
            global to_file
            src_file=f.readline().split('=')[-1][:-1]
            to_file=f.readline().split('=|')[-1].split('|')

            if to_file[-1][-1]=='\n':
                to_file[-1]=to_file[-1][:-1]
    except:
        pass
def saveini():
    try:
        with open('fd.ini','w+') as f:
            f.write('src_file=')
            f.write(src_file+'\n')
            f.write('to_file=')
            for x in to_file:
                f.write('|'+x)
    except:
        pass
def fun_select():
    global src_file
    src_file = askdirectory()
    lb_src['text']='源目录：'+src_file
def add_to_file():

    to_file.append(askdirectory())
    lb.delete(0,END)
    for file in to_file:
        lb.insert(END,file)
    saveini()

def del_to_file():

    to_file.remove(lb.get(lb.curselection()))
    lb.delete(lb.curselection())
    saveini()

def stop():
    saveini()
    lb_flag['text'] = '监控已停止'
    lb_flag['bg']='red'
    global flag
    flag=0
def startx():
    saveini()
    global file_list
    file_list=os.listdir(src_file)
    #print(file_list)
    lb_flag['text']='正在监控！'
    lb_flag['bg']='green'
    global flag
    flag=1
    t = threading.Thread(target=loop, name='LoopThread')
    t.start()
def loop():
    global flag
    while(flag):
        #print(flag)
        do_check()
        time.sleep(1)
def do_check():
    if file_list!=os.listdir(src_file):
        syn()
def syn():
    print('syn')
    file_now=os.listdir(src_file)
    for file in file_now:
        global file_list
        if not file in file_list:
            try:
                copy(file)

            except:
                lb_flag['text']='目录有错误！'
                lb_flag['bg']='red'
        #file_list=file_now
def copy(file):
    time.sleep(1)
    file_list.append(file)
    for path in to_file:
        shutil.copyfile(os.path.join(src_file,file),os.path.join(path,file))


readini()
root = Tk(className='文件分发工具-QQ619400536')
root.geometry('450x450')
root.resizable(0,0)
lb_src=Label(root,text='源目录：'+src_file,anchor='w')
lb_src.place(x=20,y=20,width=320,height=20)

select_btn=Button(root,text='选择',command=fun_select)
select_btn.place(x=350,y=18,width=50,height=30)

lb_1=Label(root,text='编辑目录')
lb_1.place(x=20,y=60)

btn_add=Button(root,text='增加目录',command=add_to_file)
btn_add.place(x=20,y=80,height=25)

btn_del=Button(root,text='删除目录',command=del_to_file)
btn_del.place(x=80,y=80,height=25)

lb = Listbox(root)
for item in to_file:
    lb.insert(END, item)
lb.place(x=20,y=110,height=240,width=380)

start_btn=Button(root,text='开始监控',command=startx)
start_btn.place(x=40,y=370,height=45,width=80)

stop_btn=Button(root,text='停止监控',command=stop)
stop_btn.place(x=300,y=370,height=45,width=80)

lb_flag=Label(root,text='监控已停止',bg='red')
lb_flag.place(x=180,y=370,width=80,height=45)

root.mainloop()

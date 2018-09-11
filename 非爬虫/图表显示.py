import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import time
import tkinter
from tkinter import *
from tkinter.filedialog import askdirectory,askopenfilename
import os
def n2m(data,m):
    x=len(data)//m
    newdata=[]
    for i in range(m):
        newdata.append(data[x*i])
    return newdata

def showPic(fname=""):
    fig, ax = plt.subplots(num="可以自定义",figsize=(10,7))
    plt.rcParams['font.sans-serif']=['SimHei']
    plt.xlabel('时间（可以改）') #横坐标标签
    plt.ylabel('大小（可以改）') #纵坐标标签
    plt.title('标题（可以改）')  #标题

    data=np.loadtxt(fname=fname,skiprows=2,usecols=(1,2,3,4),delimiter=",",encoding="GBK")
    data=np.transpose(data)
    time=np.loadtxt(fname=fname,dtype=str,skiprows=2,usecols=(0),delimiter=",",encoding="GBK")
    # print(data[1])
    # print(time)
    showNum=100
    ax.plot(n2m(time,showNum),n2m(data[0],showNum),label="输出1（自定义）", linestyle='-',marker='.')
    ax.plot(n2m(time,showNum),n2m(data[1],showNum),label="输出2", linestyle="-",marker='.')
    ax.plot(n2m(time,showNum),n2m(data[2],showNum),label="输出3", linestyle="-",marker='.')
    ax.plot(n2m(time,showNum),n2m(data[3],showNum),label="输出4", linestyle="-",marker='.')
    plt.xticks(rotation=40)
    plt.legend()
    tick_spacing = 5
    ax.xaxis.set_major_locator(ticker.MultipleLocator(tick_spacing))
    plt.show()



def fun_select():
    global src_file
    src_file = askopenfilename()
    lb_src['text']='数据文件：'+src_file

src_file=r''
root = Tk(className='自动画图工具-QQ619400536')
root.geometry('400x200')
root.resizable(0,0)
lb_src=Label(root,text='数据文件：请选择'+src_file,anchor='w')
lb_src.place(x=40,y=40,width=320,height=20)

select_btn=Button(root,text='选择',command=fun_select)
select_btn.place(x=40,y=100,width=120,height=45)


start_btn=Button(root,text='绘制图像',command=lambda :showPic(src_file))
start_btn.place(x=200,y=100,height=45,width=120)

root.mainloop()

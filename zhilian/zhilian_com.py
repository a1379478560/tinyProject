from zhilian.save  import *
from zhilian.spider import *
from tkinter import *
import datetime,time
if __name__=='__main__':
    # pos_data,p=getalldata('北京','python',3)
    # print(p)
    # save_mysql('123.206.90.65','root','130129','zhilian',pos_data)

    root = Tk(className='智联招聘岗位')
    root.geometry('900x450')
    root.resizable(0,0)

    city_label = Label(root, text='爬取城市', anchor='w')
    city_label.place(x=20, y=20, width=320, height=20)
    city_entry=Entry(root)
    city_entry.insert(0,'北京')
    city_entry.place(x=80,y=20)

    kw_label = Label(root, text='关键词', anchor='w')
    kw_label.place(x=240, y=20, width=320, height=20)
    kw_entry=Entry(root)
    kw_entry.insert(0,'会计')
    kw_entry.place(x=300,y=20)

    page_label = Label(root, text='爬取页数', anchor='w')
    page_label.place(x=450, y=20, width=320, height=20)
    page_entry=Entry(root)
    page_entry.insert(0,'5')
    page_entry.place(x=550,y=20)


    root.mainloop()
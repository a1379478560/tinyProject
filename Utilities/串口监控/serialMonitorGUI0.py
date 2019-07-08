from tkinter import *
from tkinter import messagebox
import  serial  #需要同时按照pyserial
import serial.tools.list_ports
import threading
import time
import pymysql
from queue import Queue

last_line=''
ser_list=[]
valueQueue = Queue()
flag_wait=0


class DBsaver():

    def __init__(self):
        self.tableName = "scom"
        # 打开数据库连接
        self.db = pymysql.connect("mytestdb.cxggha9emejl.ap-northeast-2.rds.amazonaws.com", "root", "a130129.", "seridb", charset='utf8')
        # 使用cursor()方法获取操作游标
        self.cursor = self.db.cursor()
        # 使用execute方法执行SQL语句
    def saveOne(self,ttime,value):
        sql = """INSERT INTO {}(timeInt,
                 valueStr)
                 VALUES ({}, "{}")""".format(self.tableName,ttime,value)
        try:
            # 执行sql语句
            self.cursor.execute(sql)
            # 提交到数据库执行
            self.db.commit()
            return 0
        except:
            # Rollback in case there is any error
            self.db.rollback()
            print("insert{} defeat.".format(value))
            return -1


    def createTable(self,tableName=None):
        if tableName:
            self.tableName=tableName
        self.cursor.execute("DROP TABLE IF EXISTS {}".format(self.tableName))
        sql = """CREATE TABLE {} (
                 id  int auto_increment primary key ,
                 timeInt BIGINT ,
                 valueStr CHAR(15)
                 )""".format(self.tableName)
        try:
            self.cursor.execute(sql)
        except:
            print(" Fail to create table {} ".format(self.tableName))
    def closedb(self):
        # 关闭数据库连接
        try:
            self.db.close()
        except:
            pass

class saverThread(threading.Thread):

    def __init__(self):
        try:
            self.db = DBsaver()
        except:
            print("Database connection failed.")
        threading.Thread.__init__(self)

    def run(self):
        while(True):
            if not valueQueue.empty():
                self.db.saveOne(*valueQueue.get())

def wait(port='COM10',baudrate=9600,bytesize=serial.EIGHTBITS):
    global flag_wait
    global valueQueue
    global ser_list
    global last_line
    if port.strip()=="0":     #端口填“0”时表示不使用这个端口
        return
    try:
        ser = serial.Serial( #下面这些参数根据情况修改
          port=port,
          baudrate=baudrate,
          # parity=serial.PARITY_ODD,
          # stopbits=serial.STOPBITS_TWO,
           bytesize=bytesize
        )
        ser_list.append(ser)
        print("开始监听:", port)
        e10.configure(state="disable")
        e11.configure(state="disable")
        e12.configure(state="disable")
        e13.configure(state="disable")
        e2.configure(state="disable")
        e3.configure(state="disable")
        start_btn.configure(state="disable")
        stop_btn.configure(state="active")
    except:
        raise
        print("打开端口{}失败，请检查端口是否存在或已被占用".format(port))
        return

    while True:
        line=ser.readline()
        try:
            line=line.decode('utf-8')
        except:
            print("{}解码失败")
            continue
        if len(line)>0:
            if line==last_line:
                print("**********************与上一个相同**********************")
            last_line=line
            valueQueue.put((time.time()*1000,line))
            print("Rsponse from {}: {}".format(port,line))

        if  not flag_wait:  #检查主线程是否要求关闭监听线程
            #print("flag_wait",flag_wait)
            #ser.close()
            print("已关闭端口{}".format(port))
            return
def waitControl(status,ports=[],baudrate=9600,bytesize=8):

    if type(baudrate)==str:
        baudrate=baudrate.strip()
        try:
            baudrate=int(baudrate)
        except:
            print("invalid baudrate",baudrate)
            return
    if type(bytesize)==str:
        bytesize=bytesize.strip()
        try:
            bytesize=int(bytesize)
        except:
            print("Invalid bytesize",bytesize)
            return

    global flag_wait
    #global ser
    global ser_list
    flag_wait=status
    if status==0:
        for ser in ser_list:
            ser.close()
        print("退出监听状态")
        e10.configure(state="normal")
        e11.configure(state="normal")
        e12.configure(state="normal")
        e13.configure(state="normal")
        e2.configure(state="normal")
        e3.configure(state="normal")
        start_btn.configure(state="active")
        stop_btn.configure(state="disable")
        return
    for port in ports:     #分别用四个线程打开四个端口
        port = port.strip()
        t2 = threading.Thread(target=wait, args=(port,baudrate,bytesize))
        t2.start()



def gui():
    global ser_list
    root = Tk(className='单片机数据保存')
    root.geometry('560x400')
    root.resizable(0, 0)

    left=50
    top=50
    rightw=280
    h=30
    w=50
    Label(root, text='端 口A', anchor='w', ).place(x=left+rightw , y=top, height=h, )
    Label(root, text='端 口B', anchor='w', ).place(x=left + rightw, y=top+2*h, height=h, )
    Label(root, text='端 口C', anchor='w', ).place(x=left + rightw, y=top+4*h, height=h, )
    Label(root, text='端 口D', anchor='w', ).place(x=left + rightw, y=top+6*h, height=h, )

    Label(root, text='波特率', anchor='w', ).place(x=left , y=top+2*h , height=h, )
    Label(root, text='数据位', anchor='w', ).place(x=left , y=top+h*4, height=h, )

    porta = StringVar()
    portb = StringVar()
    portc = StringVar()
    portd = StringVar()
    porta.set("com1")
    portb.set("com2")
    portc.set("com3")
    portd.set("com4")

    baudrate = StringVar()
    bytesize = StringVar()
    baudrate.set("9600")
    bytesize.set("8")

    global e10
    global e11
    global e12
    global e13
    global e2
    global e3
    global start_btn
    global stop_btn

    e10 = Entry(root, width=150, textvariable=porta)
    e10.place(x=left + w*2+rightw , y=top+5, height=25, width=70)
    e11 = Entry(root, width=150, textvariable=portb)
    e11.place(x=left + w*2+rightw , y=top+5+2*h, height=25, width=70)
    e12 = Entry(root, width=150, textvariable=portc)
    e12.place(x=left + w*2+rightw , y=top+5+4*h, height=25, width=70)
    e13 = Entry(root, width=150, textvariable=portd)
    e13.place(x=left + w*2+rightw , y=top+5+6*h, height=25, width=70)

    e2 = Entry(root, width=150, textvariable=baudrate)
    e2.place(x=left + w*2 , y=top+5+h*2, height=25, width=70)
    e3 = Entry(root, width=150, textvariable=bytesize)
    e3.place(x=left + w*2 , y=top+5+h*4, height=25, width=70)

    start_btn = Button(root, text='开始监听', command=lambda: waitControl(1,[e10.get(),e11.get(),e12.get(),e13.get()],e2.get(),e3.get()))
    start_btn.place(x=70, y=250, height=45, width=120)

    stop_btn = Button(root, text='停止监听', command=lambda: waitControl(0))
    stop_btn.place(x=70, y=330, height=45, width=120)
    stop_btn.configure(state="disable")
    def on_closing():
        hint='确定退出吗？'
        a=valueQueue.qsize()
        if a:
            hint='还有{}条数据尚未保存，确定退出吗？'.format(a)
        if messagebox.askokcancel("Quit",hint ):
            global flag_wait
            flag_wait=0
            time.sleep(0.5)
            for seri in ser_list:
                seri.close()
            root.destroy()
    root.protocol("WM_DELETE_WINDOW", on_closing)
    root.mainloop()
    #wait()


if __name__ == "__main__":
    threading.Thread(target=gui).start()
    saverThread().start()


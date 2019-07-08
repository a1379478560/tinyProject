from tkinter import *
import  serial  #需要同时按照pyserial
import serial.tools.list_ports
import threading

def wait(port='COM10',baudrate=9600,bytesize=serial.EIGHTBITS):
    global flag_wait
    global flag_play
    global ser
    try:
        ser = serial.Serial( #下面这些参数根据情况修改
          port=port,
          baudrate=baudrate,
          # parity=serial.PARITY_ODD,
          # stopbits=serial.STOPBITS_TWO,
           bytesize=bytesize
        )
        print("开始监听:", port)
        e1.configure(state="disable")
        e2.configure(state="disable")
        e3.configure(state="disable")
        start_btn.configure(state="disable")
        stop_btn.configure(state="active")
    except:
        #raise
        print("打开端口失败，请检查端口是否存在或已被占用")
        return


    last_line = None
    while True:
        line=ser.readline()
        line=line.decode('utf-8')
        if len(line)>0:
            if line==last_line:
                print("**********************与上一个相同**********************")
            last_line=line
            print("Rsponse : %s" % line)

        if  not flag_wait:
            #print("flag_wait",flag_wait)
            #ser.close()
            print("已关闭端口")
            return
def waitControl(status,port="com1",baudrate=9600,bytesize=8):
    port=port.strip()
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
    global ser
    flag_wait=status
    if status==0:
        ser.close()
        print("退出监听状态")
        e1.configure(state="normal")
        e2.configure(state="normal")
        e3.configure(state="normal")
        start_btn.configure(state="active")
        stop_btn.configure(state="disable")
        return
    t2 = threading.Thread(target=wait, args=(port,baudrate,bytesize))
    t2.start()



def gui():
    #wmi.WMI(namespace='wmi').WmiMonitorBrightnessMethods()[0].WmiSetBrightness(50, 0)
    root = Tk(className='单片机控制屏幕显示')
    root.geometry('280x400')
    root.resizable(0, 0)

    left=50
    top=50
    h=30
    w=50
    Label(root, text='端  口', anchor='w', ).place(x=left , y=top, height=h, )
    Label(root, text='波特率', anchor='w', ).place(x=left , y=top+2*h , height=h, )
    Label(root, text='数据位', anchor='w', ).place(x=left , y=top+h*4, height=h, )

    port = StringVar()
    baudrate = StringVar()
    bytesize = StringVar()

    port.set("com10")
    baudrate.set("9600")
    bytesize.set("8")
    global e1
    global e2
    global e3
    global  start_btn
    global stop_btn
    e1 = Entry(root, width=150, textvariable=port)
    e1.place(x=left + w*2 , y=top+5, height=25, width=70)
    e2 = Entry(root, width=150, textvariable=baudrate)
    e2.place(x=left + w*2 , y=top+5+h*2, height=25, width=70)
    e3 = Entry(root, width=150, textvariable=bytesize)
    e3.place(x=left + w*2 , y=top+5+h*4, height=25, width=70)

    start_btn = Button(root, text='开始监听', command=lambda: waitControl(1,e1.get(),e2.get(),e3.get()))
    start_btn.place(x=70, y=250, height=45, width=120)

    stop_btn = Button(root, text='停止监听', command=lambda: waitControl(0))
    stop_btn.place(x=70, y=330, height=45, width=120)
    stop_btn.configure(state="disable")
    root.mainloop()
    #wait()


if __name__ == "__main__":

    tt=threading.Thread(target=gui)
    tt.start()

from socket import *
import time
ip_port=('127.0.0.1',8080)
buffer_size=1024

udp_server=socket(AF_INET,SOCK_DGRAM)     #
udp_server.bind(ip_port)

while True:
    data,addr=udp_server.recvfrom(buffer_size)
    print(data)

    if not data:                            #判断客户端发来的的空的情况下
        fmt='%Y-%m-%d %X'                  #返回默认时间
    else:
        fmt=data.decode('utf-8')            #如果客户端输入格式就把传的值发来
    back_time=time.strftime(fmt)

    udp_server.sendto(back_time.encode('utf-8'),addr)        #把服务端的时间以encode字符串形式返回给客户端
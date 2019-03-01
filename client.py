from socket import *
ip_port=('127.0.0.1',8080)
buffer_size=1024

udp_client=socket(AF_INET,SOCK_DGRAM)

while True:
    msg=input('>>: ').strip()
    udp_client.sendto(msg.encode('utf-8'),ip_port)          #客户端发给服务端一个消息

    data,addr=udp_client.recvfrom(buffer_size)               #服务端返回的时间
    print('ntp服务器的标准时间是',data.decode('utf-8'))
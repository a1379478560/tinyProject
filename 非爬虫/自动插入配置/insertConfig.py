import os

def insert():
    fileName=''
    id=''
    sitePath=''
    serverName=''
    alias=''

    sslPath='/etc/httpd/conf.d/ssl'+id+'/'+serverName
    fileName=input("输入插入那个配置：")
    id=input("输入产品ID号：")
    sitePath=input("输入网站路径：")
    serverName=input("输入网址域名：")
    alias=input("请输入别名，不添加则直接回车：")

    with open(fileName,"r",encoding='UTF-8') as f:
        originFile=f.readlines()
        #print(originFile)
    with open("newconfig","w",encoding='UTF-8') as newFile:
        for line in originFile:
            if(line=="#130129##标志位勿动这一行##\n"):
                newFile.write(line)
                newFile.write("\n")
                newFile.write("<VirtualHost *:443>\n")
                newFile.write("\tServerAdmin "+id+'\n')
                newFile.write('\t<Directory "'+sitePath+'">\n')
                newFile.write("\tOptions -Indexes FollowSymLinks\n")
                newFile.write("\tAllow from all\n")
                newFile.write("\tAllowOverride All\n")
                newFile.write("\tOrder allow,deny\n")
                newFile.write("\t</Directory>\n")
                newFile.write("\tServerName     "+serverName+'\n')
                if(alias!=""):
                    newFile.write("\tServerAlias     " + alias + '\n')
                newFile.write("	\tDocumentRoot " + sitePath + '\n')
                newFile.write("\tSSLEngine on\n")
                newFile.write("	\tSSLCertificateFile /etc/httpd/conf.d/ssl/" + id + '/' + serverName + '/' + serverName + '.crt\n')
                newFile.write("\tSSLCertificateKeyFile /etc/httpd/conf.d/ssl/" + id + '/' + serverName + '/' + serverName + '.key\n')
                newFile.write("\tSSLCertificateChainFile /etc/httpd/conf.d/ssl/" + id + '/' + serverName + '/' + serverName + '.ca-bundle\n')
                newFile.write("</VirtualHost>")
            else:
                newFile.write(line)


if __name__=="__main__":
    while(True):
        insert()

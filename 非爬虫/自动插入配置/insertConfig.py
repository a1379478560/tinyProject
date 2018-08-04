import os

def insert():
    fileName=''
    id=''
    sitePath=''
    serverName=''
    alias=''

    while(True):
        fileName=input("输入插入那个配置文件：")
        if(fileName=="exit"):
            exit(0)
        if(os.path.exists(fileName)):
            break
        print("不存在的配置文件")
    while(True):
        id=input("输入产品ID号：")
        if(os.path.exists('/etc/httpd/conf.d/ssl/' + id)):
            break
        else:
            s=input("不存在此id对应的目录，是否自动创建？（输入yes创建，no退出，其他的重新输入id）")
            if(s=="yes"):
                os.makedirs("/etc/httpd/conf.d/ssl/" + id)
                break
            elif(s=="no"):
                exit()

    sitePath=input("输入网站路径：")
    serverName=input("输入网址域名：")
    alias=input("请输入别名，不添加则直接回车：")
    sslPath = '/etc/httpd/conf.d/ssl/' + id + '/' + serverName
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
                newFile.write("\t\tOptions -Indexes FollowSymLinks\n")
                newFile.write("\t\tAllow from all\n")
                newFile.write("\t\tAllowOverrid " + "All\n")
                newFile.write("\t\tOrder allow,deny\n")
                newFile.write("\t</Directory>\n")
                newFile.write("\tServerName     "+serverName+'\n')
                if(alias!=""):
                    newFile.write("\tServerAlias     " + alias + '\n')
                newFile.write("	DocumentRoot " + sitePath + '\n')
                newFile.write("\tSSLEngine on\n")
                newFile.write("	SSLCertificateFile "+sslPath + '/' + serverName + '.crt\n')
                newFile.write("\tSSLCertificateKeyFile "+sslPath + '/' + serverName + '.key\n')
                newFile.write("\tSSLCertificateChainFile "+sslPath + '/' + serverName + '.ca-bundle\n')
                newFile.write("</VirtualHost>")
                newFile.write("\n")
            else:
                newFile.write(line)
    os.renames(fileName,fileName+".bak")
    os.renames("newconfig",fileName)
    try:
        os.makedirs(sslPath)
    except:
        pass

if __name__=="__main__":
    while(True):
        insert()
        print("插入一条配置，不想继续插入请输入exit退出！")

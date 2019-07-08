import xlrd
import xlwt
import random
import os,sys

def writexls(data,fileName):
    if(os.path.exists(fileName)):
        ss="123"
        ss=input("已经存在随机排序过的比赛顺序文件1.xls（执行程序时请不要打开此文件），是否重新排序？重新排序请输入yes,输入其他字符不重新排序\n")
        if(ss!="yes"):
            return
    wb=xlwt.Workbook()
    sheet=wb.add_sheet("sheet1")

    for row in range(len(data)):
        for col in range(len(data[row])):
            sheet.write(row,col,data[row][col])
    wb.save(fileName)
    wb.save("顺序.xls")
    print("已经抽选出比赛顺序，顺序见本目录下  顺序.xls\n")
def readxls():
    data=[]
    workbook=xlrd.open_workbook("chengxu.et")
    sheet=workbook.sheet_by_index(0)
    rows=sheet.nrows
    for i in range(5,rows):
        data.append(sheet.row_values(i))
    #print(data)
    return data

def checkScore():
    scores=[]
    scoresNum=0
    try:
        with open("score.ini","r") as file:
            scores=file.readlines()
    except:
        print("score.ini文件丢失或损坏！")
        return -1
    if(len(scores)>=1):
        scoresNum=len(scores)
        scoresLatest=scores[-1].replace("\n","").split(" ")[0:-1]
        isReStart=input("发现已有分数数据，共有%s组分数，最后一组是%s号选手，分数是%s,清空已有数据并重新开始输入分数请输入delete，否则输入其他任意字符继续输入比赛分数\n"%(scoresNum,scoresLatest[1],scoresLatest[2:]))
        if(isReStart=="delete"):
            scoresNum=0
            with open("score.ini","w") as f:
                pass

    return scoresNum

def saveScore(num):
    wb=xlrd.open_workbook("1.xls")
    sheet=wb.sheet_by_index(0)

    while(True):
        matcher=sheet.row_values(num)

        temp=str(int(matcher[0]))+"号选手"
        print("下一个表演的是%s %s"%(temp,matcher[1:]))
        s=input("请输入分数，每个分数之间以一个空格隔开,当所有组比赛完成时，输入8888查看当前排名，输入9999结束输入：\n")
        if(s=="9999"):
            break
        if(s=="8888"):
            cal()
            continue
        s=s.replace("  "," ")
        scores=s.split(" ")
        try:
            for i in range(len(scores)):
                scores[i]=float(scores[i])
            print("输入的分数是%s\n"%(scores))
            s1111=input("确认请输入1111\n")
            if(s1111!="1111"):
                continue
        except:
            print("输入格式不正确。请检查并重新输入")
            continue
        with open("score.ini","a") as f:
            f.write(str(num)+" ")
            f.write(str(matcher[0]) + " ")
            for x in scores:
                f.write(str(x)+" ")
            f.write("\n")
        num = num + 1
def cal():
    rank=[]
    with open("score.ini","r") as f:
        scores=f.readlines()
    for x in range(len(scores)):         #序列化为数字
        scores[x]=scores[x].replace("\n","").replace(".0","")[0:-1]
        scores[x]=scores[x].split(" ")
        for y in range(len(scores[x])):
            scores[x][y]=float(scores[x][y])

    for x in scores:
        scores_one=sorted(x[2:])
        scores_one_tichu=scores_one[1:-1]
        score_one_aver=sum(scores_one_tichu)/len(scores_one_tichu)
        rank.append((x[1],round(score_one_aver,5 )))
        rank.sort(key=lambda x:x[1],reverse=True)
    print("分数排名是：\n")
    for i in range(len(rank)):
        print("第%s名是%s号选手，分数是%s"%(i+1,rank[i][0],rank[i][1]))
if __name__=="__main__":

    scores=readxls()
    random.shuffle(scores)
    writexls(scores, "1.xls")
    scoreNum=checkScore()
    if(scoreNum==-1):
        sys.exit()
    #print(scoreNum)
    saveScore(scoreNum)
    cal()
    input("输入任意字符结束程序")
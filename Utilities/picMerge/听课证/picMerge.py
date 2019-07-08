from PIL import Image,ImageDraw,ImageFont
import xlrd

def genpic(name,classs,school,id,fazhengren):
    base_img = Image.open("base.jpg")
    box = (1190, 350, 1550, 837)
    try:
        tmp_img = Image.open("pics/"+id+".jpg")
    except:
        return 1
    tmp_img=tmp_img.resize((box[2] - box[0], box[3] - box[1]))
    base_img.paste(tmp_img, box)
    ttfont = ImageFont.truetype("STZHONGS.TTF",80)
    draw = ImageDraw.Draw(base_img)
    draw.text((660-len(name)*20 ,360),name, fill=(0,0,0),font=ttfont)
    draw.text((620 -len(classs)*20,680),classs, fill=(0,0,0),font=ttfont)
    draw.text((630-len(school)*20 ,1000),school, fill=(0,0,0),font=ttfont)
    draw.text((520 ,1320),id, fill=(0,0,0),font=ttfont)
    draw.text((650 ,1570),fazhengren, fill=(0,0,0),font=ttfont)
    base_img.save("result/"+id+".png")
    print(name,id,"已完成！\n")
    return 0

def readxls(fileName):
    stuData=[]
    try:
        wb=xlrd.open_workbook(fileName)
    except FileNotFoundError:
        print("未找到学生信息.xls")
        input()
    sheet=wb.sheet_by_index(0)
    rows=sheet.nrows
    for i in range(1,rows):
        stuData.append(sheet.row_values(i))
    return rows-1,stuData

if __name__=="__main__":
    procedData=0
    needProcDat=[]
    stuNum,stuData=readxls("学生信息.xls")
    for stu in stuData:
        flag=genpic(stu[0],stu[2],stu[3],stu[1],stu[4])
        if(flag):
            needProcDat.append((stu[1],stu[0]))
        else:
            procedData+=1
    print("一共有%s条学生信息，成功处理%s条，未找到图片%s条\n"%(stuNum,procedData,len(needProcDat)))
    for x in needProcDat:
        print("姓名：%s  编号%s"%(x[1],x[0]))
    input("输入任意字符结束程序...")
from mailmerge import MailMerge
import xlrd

def merge_docx(stu_name,stu_No,class_name,seat_No):
    template="template.docx"
    document = MailMerge(template)
    #print("Fields included in {}: {}".format(template, document.get_merge_fields()))
    try:
        document.merge(
            stu_No=stu_No,
            stu_name=stu_name,
            class_name=class_name,
            seat_No=seat_No,
        )
        document.write(f"result/{stu_name}.docx")
    except:
        return 1

    return 0

def readxls(fileName):
    stuData=[]
    try:
        wb=xlrd.open_workbook(fileName)
    except FileNotFoundError:
        print(f"未找到{fileName}")
        input()
    sheet=wb.sheet_by_index(0)
    rows=sheet.nrows
    for i in range(1,rows):
        stuData.append(sheet.row_values(i))
    return stuData

if __name__=="__main__":
    proced_num=0
    failed=[]
    stu_data=readxls("收款凭证.xls")
    for stu in stu_data:
        flag=merge_docx(stu[0],stu[1],stu[2],stu[1][-2:])
        if(flag):
            failed.append((stu[0], stu[1]))
        else:
            proced_num+=1
    print(f"一共有{len(stu_data)}条学生信息，成功处理{proced_num}条，处理失败{len(failed)}条\n")
    for x in failed:
        print(f"姓名：{x[0]}  编号{x[1]}")
    input("输入任意字符结束程序...")
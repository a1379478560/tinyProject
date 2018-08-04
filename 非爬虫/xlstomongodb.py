import pymongo
import xlrd

def readxls(fileName):
    sheets={}
    wb=xlrd.open_workbook(fileName)
    sheetNames=wb.sheet_names()
    for sheetName in sheetNames:
        sheet_xls=wb.sheet_by_name(sheetName)
        sheet=[]
        rows=sheet_xls.nrows
        for i in range(rows):
            sheet.append(sheet_xls.row_values(i))
        sheets[sheetName]=sheet
    return sheets

sheets=readxls("学籍成绩.xlsx")
print(sheets)
client = pymongo.MongoClient(host='123.206.90.65', port=27017)
db=client.scores
for k,v in sheets.items():
    collection=db[k]
    for i in range(1,len(v)):
        temp = {}
        for j,name in enumerate(v[0]):
            temp[name]=v[i][j]
        result = collection.insert(temp)
from xlutils.copy import copy
import xlrd
cuo=["","×"]
cuo2=["","×","√"]
book_src = xlrd.open_workbook('cal.xlsx',)
book_des = copy(book_src)



def proxOne(sheet_src,sheet_des):
    rang=list(range(6,22))+(list(range(37,52)))
    for row in range(6,22):
        for col in reversed(range(4,11)):
            value=sheet_src.cell_value(row,col)
            if value in cuo:
                try:
                    juecha=(float(sheet_src.cell_value(4,col))*float(sheet_src.cell_value(4,col+1)))**0.5
                    lgjuecha=(float(sheet_src.cell_value(5,col))+float(sheet_src.cell_value(5,col+1)))/2
                    sheet_des.write(row,12,juecha)
                    sheet_des.write(row,14,lgjuecha)
                except:
                    print(row,col)
                    print(sheet_src.cell_value(4,col),)
                    print(sheet_src.cell_value(4,col+1))
                    raise
                break
        for col in reversed(range(4,11)):
            value = sheet_src.cell_value(row, col)
            if value in cuo2:
                try:
                    shibie = (float(sheet_src.cell_value(4, col)) * float(sheet_src.cell_value(4, col + 1))) ** 0.5
                    lgshibie=(float(sheet_src.cell_value(5,col))+float(sheet_src.cell_value(5,col+1)))/2
                    sheet_des.write(row, 13, shibie)
                    sheet_des.write(row, 15, lgshibie)
                except:
                    print(row,col)
                    print(sheet_src.cell_value(5,col),)
                    print(sheet_src.cell_value(5,col+1))
                    raise
                break
    for row in range(37,53):
        for col in reversed(range(4,11)):
            value=sheet_src.cell_value(row,col)
            if value in cuo:
                try:
                    m=float(sheet_src.cell_value(4,col))
                    n=float(sheet_src.cell_value(4,col+1))
                    juecha=(m*n)**0.5
                    lgjuecha=(float(sheet_src.cell_value(5,col))+float(sheet_src.cell_value(5,col+1)))/2
                    sheet_des.write(row,12,juecha)
                    sheet_des.write(row,14,lgjuecha)
                except:
                    print()
                    print(row,col)
                    raise
                break
        for col in reversed(range(4,11)):
            value = sheet_src.cell_value(row, col)
            if value in cuo2:
                try:
                    shibie = (float(sheet_src.cell_value(4, col)) * float(sheet_src.cell_value(4, col + 1))) ** 0.5
                    lgshibie=(float(sheet_src.cell_value(5,col))+float(sheet_src.cell_value(5,col+1)))/2
                    sheet_des.write(row, 13, shibie)
                    sheet_des.write(row, 15, lgshibie)
                except:
                    print(row,col)
                    print(sheet_src.cell_value(5,col),)
                    print(sheet_src.cell_value(5,col+1))
                    raise
                break

for i in range(26):
    print(i)
    sheet_src = book_src.sheet_by_index(i)
    sheet_des = book_des.get_sheet(i)
    proxOne(sheet_src,sheet_des)



book_des.save('res.xls')
import win32com.client
import xlrd

def readXls(fileName):
    wb = xlrd.open_workbook(fileName)
    sheet = wb.sheets()[0]
    nrows = sheet.nrows
    retData=[]
    for row in range(nrows):
        x=sheet.row_values(row, start_colx=0, end_colx=None)
        date=xlrd.xldate_as_tuple(sheet.cell(row, 4).value, 0)
        date=str(date[0])+'/'+str(date[1])+'/'+str(date[2])
        x[4]=date
        retData.append(x)
    return retData


def getConn():
    conn = win32com.client.Dispatch(r"ADODB.Connection")
    DSN = 'PROVIDER = Microsoft.Jet.OLEDB.4.0;DATA SOURCE = target.mdb'
    conn.Open(DSN)
    rs = win32com.client.Dispatch(r'ADODB.Recordset')
    rs_name = 'Analysis'
    rs.Open('[' + rs_name + ']', conn, 1, 3)
    return rs

if __name__ == '__main__':
    data=readXls("2003.xls")
    rs=getConn()
    for x in data:
        rs.AddNew()
        rs.Fields.Item(1).Value = "周日001"
        rs.Fields.Item(2).Value = x[0]
        rs.Fields.Item(3).Value = x[5]
        rs.Fields.Item(4).Value = "%.2f%.2f%.2f" %(x[10],x[11],x[12])
        rs.Fields.Item(5).Value = x[14]
        rs.Fields.Item(6).Value = str(int(x[8]))+'-'+str(int(x[9]))
        rs.Fields.Item(7).Value = x[7]
        rs.Fields.Item(8).Value = str(x[4])
        rs.Update()
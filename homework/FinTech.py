import pymysql

def conn():
    db = pymysql.connect("123.206.90.65", "root", "a130129.", "FinTech")
    cursor = db.cursor()
    cursor.execute("USE FinTech;")

    return  db

def addinvestor():
    investor_id=input("investor_id:")
    name=input("name:")
    SSN=input("SSN:")
    address=input("address:")
    db=conn()
    cursor=db.cursor()
    sql="INSERT INTO INVESTORS VALUES (%s, '%s', '%s', '%s');"%(investor_id,name,SSN,address)
    try:
        cursor.execute(sql)
        db.commit()
    except pymysql.err.IntegrityError:
        print("Add Failed")
    db.close()
def addstock():
    ticker=input("ticker:")
    company=input("company:")
    tickerclass=input("tickerclass:")
    db=conn()
    cursor=db.cursor()
    sql="INSERT INTO STOCKS VALUES ('%s', '%s','%s');"%(ticker,company,tickerclass)
    try:
        cursor.execute(sql)
        db.commit()
    except pymysql.err.IntegrityError:
        #raise
        print("Add Failed")
    db.close()

def addportfolio():
    trade_id=input("trade_id:")
    investor_id=input("investor_id:")
    ticker=input("ticker:")
    price=input("price:")
    db=conn()
    cursor=db.cursor()
    sql="INSERT INTO PORTFOLIO VALUES ('%s', '%s','%s','%s');"%(trade_id,investor_id,ticker,price)
    try:
        cursor.execute(sql)
        db.commit()
    except pymysql.err.IntegrityError:
        print("Add Failed")
    db.close()


def seeinvestor():
    db=conn()
    cursor=db.cursor()
    sql="SELECT * FROM INVESTORS;"
    try:
        cursor.execute(sql)
        result =cursor.fetchall()
        for i,row in enumerate(result):
            print(i+1,"investor_id:%s  name:%s  SSN:%s  address:%s"%row)
    except pymysql.err.IntegrityError:
        print("Error: unable to fetch data")
    cmd=input("Input 0 for return,1 for edit someone")
    if cmd=="0":
        db.close()
        return
    if cmd=="1":
        INVESTOR_ID=input("Input investorid you want to edit: ")
        name = input("name:")
        SSN = input("SSN:")
        address = input("address:")
        sql="UPDATE INVESTORS SET NAME = '%s',SSN='%s',ADDRESS = '%s' WHERE INVESTOR_ID = %s;"%(name,SSN,address,INVESTOR_ID)
        try:
            cursor.execute(sql)
            db.commit()
        except:
            print("Error: unable to update data")
    db.close()
def  seestock():
    db=conn()
    cursor=db.cursor()
    sql="SELECT * FROM STOCKS;"
    try:
        cursor.execute(sql)
        result =cursor.fetchall()
        for i,row in enumerate(result):
            print(i+1,"ticker:%s  company:%s  stock_class:%s"%row)
    except pymysql.err.IntegrityError:
        print("Error: unable to fetch data")
    cmd=input("Input 0 for return,1 for edit someone")
    if cmd=="0":
        db.close()
        return
    if cmd=="1":
        ticker=input("Input ticker you want to edit: ")
        company = input("company:")
        stock_class = input("stock_class:")
        sql="UPDATE STOCKS SET COMPANY = '%s',STOCK_CLASS = '%s' WHERE TICKER = '%s';"%(company,stock_class,ticker)
        try:
            cursor.execute(sql)
            db.commit()
        except:
            print("Error: unable to update data")
    db.close()
def seeportfolio():
    db=conn()
    cursor=db.cursor()
    sql="SELECT * FROM PORTFOLIO;"
    try:
        cursor.execute(sql)
        result =cursor.fetchall()
        for i,row in enumerate(result):
            print(i+1,"trade_id:%s  investor_id:%s  ticker:%s  price:%s"%row)
    except pymysql.err.IntegrityError:
        print("Error: unable to fetch data")
    cmd=input("Input 0 for return,1 for edit someone")
    if cmd=="0":
        db.close()
        return
    if cmd=="1":
        trade_id=input("Input trade_id you want to edit: ")
        investor_id = input("investor_id:")
        ticker = input("ticker:")
        price=input("price:")
        sql="UPDATE PORTFOLIO SET INVESTOR_ID = '%s',TICKER = '%s',PRICE=%s  WHERE TRADE_ID = %s;"%(investor_id,ticker,price,trade_id)
        try:
            cursor.execute(sql)
            db.commit()
        except:
            raise
            print("Error: unable to update data")
    db.close()

if __name__=="__main__":
    while True:
        print("Chose a Command ")
        print("0.exit")
        print("1.add investor")
        print("2.add stock")
        print("3.add portfolio")
        print("4.see or edit investor")
        print("5.see or edit stock")
        print("6.see or edit portfolio")

        cmd=input("Input a number:")
        if cmd=="0":
            break
        if cmd=="1":
            addinvestor()
        if cmd=="2":
            addstock()
        if cmd=="3":
            addportfolio()
        if cmd=="4":
            seeinvestor()
        if cmd=="5":
            seestock()
        if cmd=="6":
            seeportfolio()
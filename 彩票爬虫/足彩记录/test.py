import sqlite3

conn = sqlite3.connect('result.db')
print ("open db successful")
c = conn.cursor()
# c.execute('''CREATE TABLE yingkui
#        (
#        AA           CHAR(20) not null ,
#        BB           CHAR(20) not null ,
#        CC           CHAR(20) not null ,
#        DD           CHAR(20) not null ,
#        EE           CHAR(20) not null ,
#        FF           CHAR(20) not null ,
#        GG           CHAR(20) not null ,
#        HH           CHAR(20) not null ,
#        II           CHAR(20) not null ,
#        JJ           CHAR(20) not null ,
#        KK           CHAR(20) not null ,
#        LL           CHAR(20) not null ,
#        MM           CHAR(20) not null ,
#        NN           CHAR(20) not null ,
#        OO           CHAR(20) not null ,
#        PP           CHAR(20) not null ,
#        QQ           CHAR(20) not null ,
#        RR           CHAR(20) not null ,
#        ballNum           CHAR(20) not null ,
#        result     CHAR(20) not null );''')
c.execute("""create table yingkui(
status text not null ,
ballNum CHAR(20) not null ,
result text not null 
)
""")
c.execute("""create table zhusheng(
status text not null ,
ballNum CHAR(20) not null ,
result text not null 
)
""")
c.execute("""create table pingju(
status text not null ,
ballNum CHAR(20) not null ,
result text not null 
)
""")
print ("Table created successfully")
conn.commit()
conn.close()

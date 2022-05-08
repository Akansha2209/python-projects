import pymysql
import csv
db=pymysql.connect(host="localhost",user="root",port=3306,database='justdial',passwd="")
cursor=db.cursor()
print("connected")
f=open("G:\category\Details.csv","r")
read=csv.reader(f)
for r in read:
    Name=(r[0])
    Address=r[1]
    PhoneNumber=r[2]
    Rating=r[3]
    
    Website=r[4]
    Email=r[5]
    cmd="insert into Justdial(Name,Address,Rating,PhoneNumber,Website,Email)values(%s,%s,%s,%s,%s,%s)"
    value=(Name,Address,Rating,PhoneNumber,Website,Email)
    
    cursor.execute(cmd,value)
    db.commit()

import pymysql
db=pymysql.connect(host='localhost',port=3306,user='root',password='root',db='prodemo')
print(db)
cus=db.cursor()
#!C:\Program Files (x86)\Python38-32/python.exe
print("Content-Type: text/html\n\n")
import sys
sys.path.append('c:\\users\\mahit_3x2pbzo\\appdata\\roaming\\python\\python38\\site-packages')
import pymysql
mydb=pymysql.connect(host="localhost",user="root",password="",database="mahith")
m = mydb.cursor()
m.execute("CREATE TABLE donate(fname varchar(100), lname varchar(200), gmail varchar(200), birthday varchar(200), state varchar(200), district varchar(200), gender varchar(200), phone varchar(100), aadhar varchar(200), bloodgroup varchar(200), ml varchar(200))")
print("table created successfully")
mydb.close()

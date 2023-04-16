#!C:\Program Files (x86)\Python38-32/python.exe
print("Content-Type: text/html\n\n")
import sys
sys.path.append('c:\\users\\mahit_3x2pbzo\\appdata\\roaming\\python\\python38\\site-packages')
import pymysql
mydb=pymysql.connect(host="localhost",user="root",password="",database="mahith")
mycursor=mydb.cursor()

mycursor.execute("select * from details")
result=mycursor.fetchall()
print("<table border='2'>")
for rows in result:
    print("<tr><td>")
    print(rows)
    print("</td></tr>")
print("</table>")

#!C:\Program Files (x86)\Python38-32/python.exe
print("Content-Type: text/html\n\n")
import sys
sys.path.append('c:\\users\\mahit_3x2pbzo\\appdata\\roaming\\python\\python38\\site-packages')
import cgi, cgitb
import pymysql


mydb=pymysql.connect(host="localhost",user="root",password="",database="mahith")
mycursor=mydb.cursor()
cgitb.enable() 
form=cgi.FieldStorage()
se = form.getvalue('search')
sql="SELECT * FROM donate WHERE bloodgroup=%s"
val = (se,)
mycursor.execute(sql, val)
result=mycursor.fetchall()

print("<!DOCTYPE html><html><head><title>BLOOD BANK</title><link rel='icon' type='image/x-icon' href='icon6.jpg'><meta charset='utf-8'><meta http-equiv='X-UA-Compatible' content='IE=edge,chrome=1'/><meta content='width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=0' name='viewport'/><meta name='viewport' content='width=device-width'/><link rel='stylesheet' type='text/css' href='pro.css'><script src='C:\\xampp\\htdocs\\mahith\\pro.js' ></script><body><h1 class='head'><img  class='pic' src='blood2.jpg'  alt='image'>BLOOD BANK</h1><div class='nav'><a href='#' >&#8803;</a><a href='main.html'>Home</a><a href ='https://en.wikipedia.org/wiki/Blood_bank' target='_top' >About</a><a href ='https://indianexpress.com/about/blood-banks/' target='_top' >News</a><a href ='tel:7207909030'>Contact</a><a href='https://www.google.com/maps/search/blood+bank+about/@17.7013496,83.1028318,11z/data=!3m1!4b1?hl=en-US' target='_top'>Maps</a><a href='donate.html'>Donate</a>	<button  id='dark' onclick='myFunction()' class='button' >Dark mode</button><form action='search.py' method='POST' class='search'><input type='search'  name='search'placeholder='Search...'aria-label='Search through site content'><button type='submit'>Search</button></form></div><marquee id='mark'>important updates are here....!</marquee>")
'''print("<table style='border:1px solid black;margin-left:auto;margin-right:auto;'><tr><th><b>NAME</b></th>&nbsp&nbsp<th><b>Gmail</b></th>&nbsp&nbsp<th><b>DATE OF BIRTH</b></th>&nbsp&nbsp<th><b>State</b></th>&nbsp&nbsp<th><b>District</b></th>&nbsp&nbsp<th><b>Gender</b></th>&nbsp&nbsp<th><b>Phone no</b></th>&nbsp&nbsp<th><b>Aadhar no</b></th>&nbsp&nbsp<th><b>Blood group</b></th>&nbsp&nbsp<th><b>M/L</b></th>&nbsp&nbsp")'''
'''for rows in result:
        print("<table style='border:1px solid black;margin-left:auto;margin-right:auto;'>")
        print("<tr><td style='border:1px solid black;'></td></tr>")
        print(rows)
        
        
        print("</table>")
 
        print("<table border=2px solid black>")
        print("<tr><td>name</td><td>",rows[i],"</td></tr>")
        print("</table>")'''
print("<!DOCTYPE html>")
print("<html><head><style>table{table-collapse:collapse;padding:2px;}tr:nth-child(odd){background-color:blue;}tr:nth-child(even){background-color:yellow;}</style></head><body><table border:2px solid black style='position:relative; left:20%;>'")

print("<tr><th>fname</th><th>lname</th><th>gmail</th><th>birthdate</th><th>state</th><th>district</th><th>gender</th><th>phoneno</th><th>aadhar</th><th>bloodgroup</th><th>ml</th></tr>")
       
    
for row in result:
    print("<tr><td>",row[0],"</td>""<td>",row[1],"</td>""<td>",row[2],"</td>""<td>",row[3],"</td>""<td>",row[4],"</td>""<td>",row[5],"</td>""<td>",row[6],"</td>""<td>",row[7],"</td>""<td>",row[8],"</td>""<td>",row[9],"</td>""<td>",row[10],"</td></tr>")
        
    
    '''print("<table border=2px solid black style='position:relative; left:50%;'")
    print("<tr><td>fname</td><td>",row[0],"</td></tr>")
    print("<tr><td>lname</td><td>",row[1],"</td></tr>")
    print("<tr><td>gmail</td><td>",row[2],"</td></tr>")
    print("<tr><td>birthdate</td><td>",row[3],"</td></tr>")
    print("<tr><td>state</td><td>",row[4],"</td></tr>")
    print("<tr><td>district</td><td>",row[5],"</td></tr>")
    print("<tr><td>gender</td><td>",row[6],"</td></tr>")
    print("<tr><td>phno</td><td>",row[7],"</td></tr>")
    print("<tr><td>aadhar</td><td>",row[8],"</td></tr>")
    print("<tr><td>bloodgroup</td><td>",row[9],"</td></tr>")
    print("<tr><td>ml</td><td>",row[10],"</td></tr>")
    print("</table>")'''

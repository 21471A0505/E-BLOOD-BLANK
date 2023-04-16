#!C:\Program Files (x86)\Python38-32/python.exe
print("Content-Type: text/html\n\n")
import sys
sys.path.append('c:\\users\\mahit_3x2pbzo\\appdata\\roaming\\python\\python38\\site-packages')
import cgi, cgitb
import pymysql
cgitb.enable() 

form=cgi.FieldStorage()
fn = form.getvalue('fname')
ln = form.getvalue('lname')
gm = form.getvalue('mail')
bt = form.getvalue('birthday')
st = form.getvalue('state')
dt = form.getvalue('district')
gd = form.getvalue('gender')
ph = form.getvalue('phone')
aa = form.getvalue('aadhar')
bg = form.getvalue('bloodgroup')
Ml = form.getvalue('ml')



con=pymysql.connect(user='root',password='',host='localhost',database='mahith')
cur=con.cursor()
sql = "INSERT INTO donate (fname,lname,gmail,birthday,state,district,gender,phone,aadhar,bloodgroup,ml) VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
val = (fn, ln, gm, bt, st, dt, gd, ph, aa, bg, Ml)
cur.execute(sql, val)
con.commit()
con.close()


print("<h1 style='margin-left:390px;color:green;'>You have donted blood Successfully</h1>")
print("<body style=margin:90px 90px 90px 90px;padding-left:50px;background-position:center;><div style='border:15px solid #c06871;text-align:center;'><br><br><br><h2 style='color:#c06871;text-align:center;'>An Organization</h2><h1 style='color:#c06871;text-align:center;font-size:70px;'>Certificate of Completion</h1><br><br><h1 style='text-align:center;font-size:40px'>This certificate is presented to</h1><div style:'margin:40px;'><br><h1 style='text-aling:center;text-size:20px;'>")
print(fn,ln)
print("</h1><hr></div> <h1 style='text-aling:center;'>For donating of blood </h1></div></body>")
print("<br><br><div style='text-align:center;margin-left:50px;'><button onclick='window.print()'>Download</button></div>")





#print("<h3 style='margin-left:520px;color:blue'>CLICK HERE TO <a href='main.html'> login</a></h3></body>")


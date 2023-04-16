#!C:\Program Files (x86)\Python38-32/python.exe
print("Content-Type: text/html\n\n")
import sys
sys.path.append('c:\\users\\mahit_3x2pbzo\\appdata\\roaming\\python\\python38\\site-packages')
import cgi, cgitb
import pymysql
cgitb.enable()
mydb=pymysql.connect(user='root',password='',host='localhost',database='mahith')
mycursor=mydb.cursor()
form=cgi.FieldStorage()
mycursor.execute("select * from details")
result=mycursor.fetchall()
maillist=[]
for row in result:
    maillist.append(row[2])
gmail = form.getvalue('gmail')
password = form.getvalue('pwd')
if gmail in maillist:
    i=maillist.index(gmail)
    row=result[i]
    if (row[4]==password):
        print("<!DOCTYPE html><html><head><title>BLOOD BANK</title><link rel='icon' type='image/x-icon' href='icon6.jpg'><meta charset='utf-8'><meta http-equiv='X-UA-Compatible' content='IE=edge,chrome=1'/><meta content='width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=0' name='viewport'/><meta name='viewport' content='width=device-width'/><link rel='stylesheet' type='text/css' href='pro.css'><script src='C:\\xampp\\htdocs\\mahith\\pro.js' ></script><body><h1 class='head'><img  class='pic' src='blood2.jpg'  alt='image'>BLOOD BANK</h1><div class='nav'><a href='#' >&#8803;</a><a href='main.html'>Home</a><a href ='https://en.wikipedia.org/wiki/Blood_bank' target='_top' >About</a><a href ='https://indianexpress.com/about/blood-banks/' target='_top' >News</a><a href ='tel:7207909030'>Contact</a><a href='https://www.google.com/maps/search/blood+bank+about/@17.7013496,83.1028318,11z/data=!3m1!4b1?hl=en-US' target='_top'>Maps</a><a href='donate.html'>Donate</a><a href='bot.html'>Boot</a><button  id='dark' onclick='myFunction()' class='button' >Dark mode</button><form action='search.py' method='POST' class='search'><input type='search'  name='search'placeholder='Search...'aria-label='Search through site content'><button type='submit'>Search</button></form></div><marquee id='mark'>important updates are here....!</marquee><table style='border:2px solid black;margin-left:auto;margin-right:auto;'><tr><th>SI</th><th>District</th><th>Name of the blood bank</th><th>Blood Bank Incharge</th></tr><tr><td>1</td><td>kolkata</td><td>Institute of Blood Transfusion Medicine & Immuno Haematology (Central Blood Centre) - BCSU</td><td>Dr. Swapan Saren, Director - 033 2351 0620</td></tr><tr ><td>2</td><td>ap</td><td>SSKM Hospital Blood Centre - BCSU</td><td>Dr. Pratik Dey, MOIC - 033 2204 12333</td></tr><tr><td>3</td><td>ts</td><td>R.G. Kar Medical College & Hospital Centre - BCSU</td><td>Dr. Malay Ghosh, MOIC - 6291661411</td></tr><tr><td>4</td><td>rajstan</td><td>Dr.B.C.Roy PGIPS Blood Centre - BCSU</td><td>Dr. Sukumar Dutta, MOIC -9432305174</td></tr><tr><td>5</td><td>odisha</td><td>M.R. Bangur Dist. Hospital Blood Centre</td><td>Dr. Krishna Kanta Barui, MOIC - 9474044939</td></tr><tr><td>6</td><td>gujarath</td><td>Canning S.D.Hospital Blood Centre</td><td>Dr. Tanmoy Ray, MOIC - 9434319374/ 8820731069</td></tr><tr><td>7</td><td>tamilnadu</td><td>Medinipur Medical College & Hospital Blood Centre - BCSU</td><td>Dr. Basori Mohan Maity, MOIC - 03222 261007/ 7407201505</td></tr><tr><td>8</td><td>madhyapradesh</td><td>Ghatal S.D.Hospital Blood Centre</td><td>Dr. Durga Sankar Das, MOIC - 9474896980</td></tr><tr><td>9</td><td>kerala</td><td>Ghatal S.D.Hospital Blood Centre</td><td>Dr. Durga Sankar Das, MOIC - 9474896980</td></tr><tr><td>10</td><td>gova</td><td>Gopiballavpur SSH Blood Centre</td><td>Dr. Kartick Naskar, MOIC - 9734658881</td></tr><tr><td>11</td><td>madhyapradesh</td><td>Barjora SSH Blood Centre</td><td>Dr. Parna Bhoumik, MOIC - 9477583834/ 9433390876</td></tr><tr><td>12</td><td>uttarpradesh</td><td>Serampore S.D.Hospital (Walsh) Blood Centre</td><td>Dr. Pranabesh Mukherjee, MOIC - 9804368822</td></tr><tr><td>13</td><td>manipur</td><td>Gandhi Memorial Hospital Blood Centre</td><td>Dr. Somnath Sarkar, MOIC - 9836697620</td></tr></table>")
        
        
        print("<body style='background-color:grey;'</body>")
        '''print("<h2 style='color:green;margin-left:550px;'>Login Successfully...</h2>")
        print("<h2 style='color:green;margin-left:550px;'>Welcome,"+row[0]+row[1]+"</h2>")
        print("<h2 style=margin-left:550px;><a href=pro121.html>Click here to go to home page</a></h2>")'''
    else:
        print("please check you user and password")
      
         
else:  
    print("user does not exist")
    







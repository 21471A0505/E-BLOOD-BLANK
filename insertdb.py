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
pw = form.getvalue('pwd')

pw1 = form.getvalue('pwd1')
bd = form.getvalue('birthday')
gd = form.getvalue('gender')
ph = form.getvalue('phone')
aa = form.getvalue('aadhar')
bg = form.getvalue('bloodgroup')



con=pymysql.connect(user='root',password='',host='localhost',database='mahith')
cur=con.cursor()
sql = "INSERT INTO details (fname,lname,gmail,password,repassword,birthday,gender,phone,aadhar,bloodgroup) VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
val = (fn, ln, gm, pw, pw1, bd, gd, ph, aa, bg)
cur.execute(sql, val)
con.commit()
con.close()

'''print("<body style=background-image:url('register.png');background-repeat:no-repeat;margin:90px;padding-left:50px;background-position:center;></body>")
print("<h1 style='margin-left:390px;color:green'>You have Registered Successfully</h1>")'''
import js2py
print("<!DOCTYPE html><html><head><title>BLOOD BANK</title><link rel='icon' type='image/x-icon' href='icon6.jpg'><meta charset='utf-8'><meta name='viewport' content='width=device-width, initial-scale=1'><link rel='stylesheet' href='one.css' type='text/css'><script>window.alert('you have register successfully');let slideIndex = 0;showSlides();function showSlides() {let i;let slides = document.getElementsByClassName('mySlides');for (i = 0; i < slides.length; i++) {slides[i].style.display = 'none';  }slideIndex++if (slideIndex > slides.length) {slideIndex = 1}    slides[slideIndex-1].style.display = 'block';  setTimeout(showSlides, 4000); }function openForm() {document.getElementById('myForm').style.display = 'block';document.getElementById('mySlides fade').style.filter='blur(8px)';}function closeForm() {document.getElementById('myForm').style.display = 'none';}var modal = document.getElementById('id01');window.onclick = function(event) {if (event.target == modal) {modal.style.display = 'none';}}</script></head><body style='background-color:#40E0D0;'><ul><li><a href='https://en.wikipedia.org/wiki/Blood_bank' ><b>About</b></a></li><li><a href='' onclick='document.getElementById('id01').style.display='block'' style='width:auto;'><b>Register</b></a></li><li><a href='main.html' onclick='return openForm();' ><b>Login</b></a></li></ul><div class='form-popup' id='myForm'><form action='validation.py' method='POST' class='form-container' autocomplete='off'><h1>Login</h1><label for='email'><b>Email</b></label><input type='text' id='email' placeholder='Enter Email' name='gmail' required><label for='psw'><b>Password</b></label><input type='password' id='psw' placeholder='Enter Password' name='pwd' required><button type='submit' class='btn'>Login</button><button type='button' class='btn cancel' onclick='closeForm()' >Close</button></form></div><div class='slideshow-container'><div class='mySlides fade'><img src='blood21.jpg'style='width:100%;height:50%;'></div><div class='mySlides fade'><img src='p4.jpg' style='width:100%;height:80%;'></div><div class='mySlides fade'><img src='blood12.jfif' style='width:100%;height:80%;'></div><div class='mySlides fade'><img src='dark14.jpg' style='width:100%;height:80%;'></div></div><div id='id01' class='modal'><form action='insertdb.py' method='POST' class='modal-content animate' autocomplete='off'><div class='imgcontainer'><span onclick='document.getElementById('id01').style.display='none'' class='close' title='Close Modal'>&times;</span><img src='login.png' alt='Avatar' class='avatar'></div><div class='container'><label for='fname'><b>First name:</b></label><input type='text' id='fname' name='fname' placeholder='Enter first name' required><br><br><label for='lname'><b>Last name:<b></label><input type='text' id='lname' name='lname'  placeholder='Enter last name'required><br><br><label for='password'><b>Password:</b></label><input type='password' id='password' name='pwd'  placeholder='123@ma'required><br><br><label for='password1'><b>Repeat Password:</b></label><input type='password' id='password1' name='pwd1'  placeholder='123@ma'required><br><br><label for='aadhar'><b>Aadhar no:</b></label><input type='text' id='aadhar' name='aadhar'  placeholder='Enter aadhar no' required><br><br><label><b>Gender:</b></label><input type='radio' id='male' name='gender' value='Male'><label for='male'>Male</label><input type='radio' id='Female' name='gender' value='Female'><label for='female'>Female</label><input type='radio' id='others' name='gender' value='others'><label for='others'>Others</label>&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp<label for='birthday'><b>Birthday:</b></label><input type='date' id='birthday' name='birthday' required><br><br><label for='gmail'><b>Gmail:</b></label><input type='email' id='gmail' name='mail'  placeholder='abc@gmail.com'required>&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp<label for='phone'><b> Phone no:<b></label><input type='tel' id='phone' name='phone' placeholder='1234567890' pattern='[0-9]{10}' required><br><br><label><b>Blood Group:</b></label><input list='bloodgroup' name='bloodgroup'><datalist id='bloodgroup'><option value='A positive (A+)''><option value='A negative (A-)'><option value='B positive (B+)'><option value='B negative (B-)'><option value='O positive (O+)'><option value='O negative (O-)'><option value='AB positive (AB+)'><option value='AB negative (AB-)'></datalist><br><br><p>By creating an account you agree to our <a href='#'>Terms&Privacy.</a></p><button type='submit'>Register</button></div<div class='container' style='background-color:#f1f1f1'><button type='button' onclick='document.getElementById('id01').style.display='none'' class='cancelbtn'>Cancel</button><span class='psw'>Already have an account?<a href='main.html'>Sign in</a></span></div></form></div><script>window.alert('you have register successfully');let slideIndex = 0;showSlides();function showSlides() {let i;let slides = document.getElementsByClassName('mySlides');for (i = 0; i < slides.length; i++) {slides[i].style.display = 'none';  }slideIndex++;if (slideIndex > slides.length) {slideIndex = 1}    slides[slideIndex-1].style.display = 'block';  setTimeout(showSlides, 4000); // Change image every 2 seconds}function openForm() {document.getElementById('myForm').style.display = 'block';document.getElementById('mySlides fade').style.filter='blur(8px)';function closeForm() {document.getElementById('myForm').style.display = 'none';}var modal = document.getElementById('id01');window.onclick = function(event) {if (event.target == modal) {modal.style.display = 'none';}}</script></body></html>")


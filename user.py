#two functions- checkUser() for login and addUser() for signup
#create session with userId as soon as the the user logs in
import re


from flask import Flask, redirect,  url_for, render_template, request,flash, session
#from mainurls import *
import sqlite3 as sql

#def checkuser():
 #  us=request.form['username1']
  # ps=request.form['password1']

def checkuser():
   msg=''
   if request.method == 'POST':
      un1 = request.form.get('username1')
      pwd = request.form.get('password1')       
      with sql.connect("counselling.db") as con:
         cur = con.cursor()
         cur.execute("SELECT UserId,Password FROM User where Email = (?)",[un1])
         valemail = cur.fetchone()
         try:
            session['usrid']=valemail[0]
            if pwd == valemail[1]:
               usrid = session['usrid'] 
               return render_template('home.html') 
            else:
               flash('Looks like you are not registered') 
               return render_template('login.html')
         except:
           flash('Looks like you are not registered')
           return render_template('login.html')



def adduser():
   msg=''
   if request.method == 'POST':
      try:
         nm = request.form.get('Name')
         em = request.form.get('username')    
         tpass = request.form.get('tpassword')    
         passw = request.form.get('password')
         gen = request.form.get('gender')
         dateob = request.form.get('dob')
         cl = request.form.get('class')
         dep = request.form.get('Dept')       
         with sql.connect("counselling.db") as con:
            cur = con.cursor()
            cur.execute("SELECT Email FROM User")
            uname= cur.fetchall()     
            for i in uname:
              if em in i:
                  raise Exception
              else:  
                  cur.execute("INSERT INTO User (Email,Name,Password,DOB,Gender,Class,Department)  VALUES (?,?,?,?,?,?,?)",[em,nm,passw,dateob,gen,cl,dep] ) 
                  con.commit()
                  msg = "Record successfully added"
      except Exception:         
         con.rollback()
         msg = "username already taken, try again with another user name"
      except:
         con.rollback()
         msg = "error in insert operation"
      
      finally:
        con.close()
        return render_template("login.html",msg = msg)


        
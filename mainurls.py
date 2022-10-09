
from crypt import methods
from tokenize import String
from flask import Flask, redirect, url_for, render_template, request,flash,session
import sqlite3 as sql
from user import *

from flask_session import Session

app=Flask(__name__)
app.secret_key = "stucons"


@app.route('/signup',methods=['POST','GET'])
def signup():
    return render_template('signup.html')
@app.route('/signed',methods=['POST'])
def signedin():
    return adduser() 

@app.route('/')
@app.route('/login',methods=['POST','GET'])
def login():
    return render_template('login.html')

@app.route('/logged',methods=['POST'])
def loggedin():
    return checkuser()

@app.route('/home', methods=['POST','GET'])
def home():
    return render_template('home.html')

@app.route('/questionnaire')
def questions():
    return render_template('ques.html')


@app.route('/report/<int:acad>/<int:adj>/<int:social>/<int:fam>/<int:health>')
def generateReport( acad: int, adj: int, social: int, fam: int, health: int ):
    return render_template('report.html')

@app.route('/profile')
def profile():
    return render_template('profile.html')

@app.route('/logout')
def logout():
    session["userId"] = None
    return redirect("/")


if __name__=='__main__':
    app.run(debug=True)














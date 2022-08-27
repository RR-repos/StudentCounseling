from flask import Flask, redirect, url_for, render_template, request,flash,session
import sqlite3 as sql

app=Flask(__name__)

@app.route('/signup')
def signup():
    return render_template('signup.html')

@app.route('/')
@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/questionnaire')
def questions():
    return render_template('ques.html')


@app.route('/report/<int:acad>/<int:adj>/<int:social>/<int:fam>/<int:health>')
def generateReport(acad:int,adj:int,social:int,fam:int,health:int):
    return render_template('ques.html')

@app.route('/profile')
def profile():
    return render_template('profile.html')

@app.route('/logout')
def logout():
    return render_template('login.html')

if __name__=='__main__':
    app.run(debug=True)













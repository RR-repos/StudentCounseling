#CRUD operations
#Create a new report- link to questionaire
#Read- display user data using userId from session and quering the db
#Update- update user data using userId from session and quering the db
#Delete- delete the report using userId from session and quering the db
import re
from flask import Flask, redirect,  url_for, render_template, request,flash, session
from mainurls import *
import sqlite3 as sql

def profdata():
    if request.method == 'GET':
        usrid = session['usrid']
        with sql.connect("counselling.db") as con:
            cur = con.cursor()
            cur.execute("SELECT* FROM User WHERE UserId=(?)",[usrid])
            udata = cur.fetchall()
        con.close()
        return render_template('profile.html',udata=udata)
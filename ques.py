#calculate different scores, check scoring scheme- https://docs.google.com/document/d/1BKUZlRhjtckP8GE7OKepq_7KMr8xX5p483xrNK2SeeM/edit
#for the questions- https://docs.google.com/spreadsheets/d/1nXtuT1f3q4WXAySqABIigc0tZGIFY8_jz6fiUTWZ68w/edit#gid=0
from flask import redirect, url_for, render_template, request,flash,session
from models import *
def showQuest():
    quest=questions.query.all()
    return render_template('ques.html',quest=quest)
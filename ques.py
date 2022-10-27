#calculate different scores, check scoring scheme- https://docs.google.com/document/d/1BKUZlRhjtckP8GE7OKepq_7KMr8xX5p483xrNK2SeeM/edit
#for the questions- https://docs.google.com/spreadsheets/d/1nXtuT1f3q4WXAySqABIigc0tZGIFY8_jz6fiUTWZ68w/edit#gid=0
import re
from flask import Flask, redirect,  url_for, render_template, request,flash, session
from mainurls import *
from report import *
import sqlite3 as sql

def quesList():
    try:
        q1= int(request.form.get('q1'))
        q2= int(request.form.get('q2'))
        q3= int(request.form.get('q3'))
        q4= int(request.form.get('q4'))
        q5= int(request.form.get('q5'))
        q6= int(request.form.get('q6'))
        q7= int(request.form.get('q7'))
        q8= int(request.form.get('q8'))
        q9= int(request.form.get('q9'))
        q10= int(request.form.get('q10'))
        q11= int(request.form.get('q11'))
        q12= int(request.form.get('q12'))
        q13= int(request.form.get('q13'))
        q14= int(request.form.get('q14'))
        q15= int(request.form.get('q15'))
        q16= int(request.form.get('q16'))
        q17= int(request.form.get('q17'))
        acad= q1+q2+q3+q4+q5+q6+q7+q8+q9+q10+q11+q12+q13+q14+q15+q16+q17 

        q18= int(request.form.get('q18'))
        q19= int(request.form.get('q19'))
        q20= int(request.form.get('q20'))
        q21= int(request.form.get('q21'))
        q22= int(request.form.get('q22'))
        q23= int(request.form.get('q23'))
        q24= int(request.form.get('q24'))
        q25= int(request.form.get('q25'))
        q26= int(request.form.get('q26'))
        adj=q18+q19+q20+q21+q22+q23+q24+q25+q26

        q27= int(request.form.get('q27'))
        q28= int(request.form.get('q28'))
        q29= int(request.form.get('q29'))
        q30= int(request.form.get('q30'))
        q31= int(request.form.get('q31'))
        q32= int(request.form.get('q32'))
        q33= int(request.form.get('q33'))
        q34= int(request.form.get('q34'))
        q35= int(request.form.get('q35'))
        social=q27+q28+q29+q30+q31+q32+q33+q34+q35

        q36= int(request.form.get('q36'))
        q37= int(request.form.get('q37'))
        q38= int(request.form.get('q38'))
        q39= int(request.form.get('q39'))
        q40= int(request.form.get('q40'))
        q41= int(request.form.get('q41'))
        q42= int(request.form.get('q42'))
        fam =q36+q37+q38+q39+q40+q41+q42

        q43= int(request.form.get('q43'))
        q44= int(request.form.get('q44'))
        q45= int(request.form.get('q45'))
        q46= int(request.form.get('q46'))
        q47= int(request.form.get('q47'))
        q48= int(request.form.get('q48'))
        q49= int(request.form.get('q49'))
        q50= int(request.form.get('q50'))
        q51= int(request.form.get('q51'))
        q52= int(request.form.get('q52'))
        health= q43+q44+q45+q46+q47+q48+q49+q50+q51+q52
        return gen(acad=acad,adj=adj,social=social,fam=fam,health=health)

    except Exception as e:
        return render_template('ques.html',msg=e)



#taking the scores, normalize them and plot a bargraph
# check https://docs.google.com/document/d/1BKUZlRhjtckP8GE7OKepq_7KMr8xX5p483xrNK2SeeM/edit#
import matplotlib.pyplot as plt
import re
from flask import Flask, redirect,  url_for, render_template, request,flash, session
from mainurls import *
import sqlite3 as sql

def gen(acad, adj, social, fam, health):
    # creating the dataset
    nacad=((acad*100)/17)
    nadj=((adj*100)/9)
    nsocial=((social*100)/10)
    nfam=((fam*100)/7)
    nhealth=((health*100)/9)
    data = {'academic':nacad, 'personality/adjustment':nadj, 'social':nsocial,'family':nfam,'clinical/health':nhealth} 

    courses = list(data.keys())
    values = list(data.values())
    
    fig = plt.figure(figsize = (10, 5))
    
    # creating the bar plot
    plt.bar(courses, values, color ='lightgreen',width = 0.4)
    plt.savefig("bargraph.png",bbox_inches='tight')
    return render_template('report.html')
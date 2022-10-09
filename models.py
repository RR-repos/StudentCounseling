import os

from flask import Flask
import flask_sqlalchemy
from flask_sqlalchemy import SQLAlchemy
from mainurls import db

   
class questions(db.Model):
    __tablename__="questions"
    qid = db.Column(db.Integer, primary_key=True)
    category =db.Column(db.String, nullable=False)
    question =db.Column(db.String, nullable=False)
    
    
from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SECRET_KEY']='d0de5f40bd978ffceb1e7d3b247b0700'
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///projetc6.db'

db=SQLAlchemy(app)

from projetc6 import routes


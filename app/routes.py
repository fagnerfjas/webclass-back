from app import app
from flask import render_template, redirect, url_for
from app.db import Connect

database = Connect(app)

@app.route('/')
@app.route('/index')
def index():    
    return render_template('index.html')


@app.route('/databases')
def databases():
    return database.databases()

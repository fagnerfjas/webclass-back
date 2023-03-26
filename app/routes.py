from app import app
from flask import render_template, redirect, url_for, request
from app.db import Connect

database = Connect(app)

#   Initial page
@app.route('/')
@app.route('/index')
def index():    
    return render_template('index.html')


#   Return a JSON with all databases
@app.route('/databases')
def databases():
    return str(database.databases())

#   Return a JSON with all databases, respective tables and yours descriptions fields
@app.route('/desc_databases', methods=['GET'])
def desc_all_tables():
    return str(database.descAllDatabases())    


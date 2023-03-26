from app import app
from flask import render_template, redirect, url_for, request
from app.db import Connect

database = Connect(app)

@app.route('/')
@app.route('/index')
def index():    
    return render_template('index.html')


@app.route('/databases')
def databases():
    return database.databases()


@app.route('/desc_all_tables', methods=['GET'])
def desc_all_tables():
    return database.descAllDatabases()
    #return database.tables( request.args.get('database') )


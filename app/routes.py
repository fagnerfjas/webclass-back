from app import app
from flask import render_template, redirect, url_for, request
from app.db import Connect
import json

database = Connect(app)

#   Initial page
@app.route('/')
@app.route('/index')
def index():    
    return render_template('index.html')


#   Return a JSON with all databases
@app.route('/databases')
def databases():
    return json.dumps(database.databases())


#   Return a JSON with all tables of one database
@app.route('/tables/<db_name>', methods=['GET'])
def tables(db_name):
    # db_name = request.args.get('database')
    tables = database.tables( db_name )
    list_tables = []
    for table in tables:
        list_tables.append( table['Tables_in_{}'.format(db_name)] )
    return json.dumps(list_tables)


#   Return a describe for a table in on database
@app.route('/desc_table/<db_name>/<table_name>', methods=['GET'])
def describeTables(db_name, table_name):
    data = database.descTable(db_name, table_name)
    return json.dumps(data)



#   Return a JSON with descriptions of the especific database
@app.route('/desc_database/<db_name>', methods=['GET'])
def desc_database(db_name):
    return json.dumps( database.descDatabase(db_name) )    



#   Return a JSON with all databases, respective tables and yours descriptions fields
@app.route('/desc_databases', methods=['GET'])
def desc_all_databases():
    return str(database.descAllDatabases())    


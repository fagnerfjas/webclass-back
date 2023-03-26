###
### @author Fagner Jefferson 
### fagnerfjas@gmail.com

from flask_mysqldb import MySQL
from config import db
import json

class Connect:

    ### Initial configuration for conect on database
    def __init__(self, app):
        app.config["MYSQL_HOST"] = db.DB_HOST
        app.config["MYSQL_USER"] = db.DB_USER
        app.config["MYSQL_PASSWORD"] = db.DB_PASSWORD
        app.config["MYSQL_DB"] = db.DB_NAME
        # Extra configs, optional:
        app.config["MYSQL_CURSORCLASS"] = "DictCursor"
        app.config["MYSQL_CUSTOM_OPTIONS"] = {"ssl": {"ca": "/path/to/ca-file"}}  # https://mysqlclient.readthedocs.io/user_guide.html#functions-and-attributes
        #variable of global for connection
        self.mysql = MySQL(app)


     
    #   Return all databases    
    def databases(self):
        cur = self.mysql.connection.cursor()
        cur.execute("""show databases""")
        dbs = cur.fetchall()
        return dbs



    ##  Return a list witch all tables in a database
    def tables(self, database):
        cur = self.mysql.connection.cursor()
        cur.execute("show tables in  {}".format(database))
        tables = cur.fetchall()
        return tables



    ## Return a list formated with describe of the table
    def descTable(self, database, table):
        cur = self.mysql.connection.cursor()
        cur.execute("desc  {}.{}".format(database, table))
        describe = cur.fetchall()
        return list(describe)

    

    ## Return the number of register in specific table
    def countRegisters(self, database, table):
        cur = self.mysql.connection.cursor()
        cur.execute("select count(*) from  {}.{}".format(database, table))
        qtd = cur.fetchall()
        return qtd[0]['count(*)']



    ##  Return the informations of all tables in a database, 
    ##  including number of retisters, name of the table structure description.
    def descDatabase(self, database):        
        allDatas = {}        
        tables = self.tables( database )
        allDatas = {
                'db_name': database,
                'tables': {}
            }
        
        for table in tables:
            table_name = table['Tables_in_{}'.format(database)]
            descriptions = self.descTable(database, table_name)
            count = self.countRegisters(database, table_name)
            allDatas['tables'][table_name] = {
                'table_name': table_name,
                'count': count,
                'describe': descriptions
            }
        return allDatas



    ##  Return one dictionary with all databases, 
    ##  for each database, they have a dictionary with 
    ##  descriptions of each table.
    def descAllDatabases(self):
        databases = self.databases()
        allDatas = {}
        for datab in databases:
            db_name = datab['Database']
            if db_name not in db.DB_EXCLUDE:
                allDatas[ db_name ] = self.descDatabase(db_name)
        return allDatas
        
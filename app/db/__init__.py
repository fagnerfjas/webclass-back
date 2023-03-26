###
### @author Fagner Jefferson 
### fagnerfjas@gmail.com

from flask_mysqldb import MySQL
from config import db

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


     
    #   Return all databases in this connection    
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


    ## Return a describe of the a table
    def descTable(self, database, table):
        cur = self.mysql.connection.cursor()
        cur.execute("desc  {}.{}".format(database, table))
        describe = cur.fetchall()
        return describe

    
    ## Return the number of register on specific table
    def countRegisters(self, database, table):
        cur = self.mysql.connection.cursor()
        cur.execute("select count(*) from  {}.{}".format(database, table))
        qtd = cur.fetchall()
        return qtd[0]['count(*)']


    ##  Return a Json with descriptions of all tables in all databases.
    def descAllDatabases(self):
        databases = self.databases()
        allDatas = {}
        for datab in databases:
            if datab['Database'] not in db.DB_EXCLUDE:
                database_name = datab['Database']
                tables = self.tables( database_name )
                allDatas[database_name] = {
                        'db_name': database_name,
                        'tables': {}
                    }
                
                for table in tables:
                    table_name = table['Tables_in_{}'.format(database_name)]
                    descriptions = self.descTable(database_name, table_name)
                    count = self.countRegisters(database_name, table_name)
                    allDatas[database_name]['tables'] = {
                        'table_name': table_name,
                        'count': count,
                        'describe': descriptions
                    }                    
        return allDatas
        


    # def select(self):
    #     cur = self.mysql.connection.cursor()
    #     cur.execute("""SELECT * FROM users limit 10""")
    #     rv = cur.fetchall()
    #     return str(rv)

    # def selectTable(self, table):
    #     cur = self.mysql.connection.cursor()
    #     cur.execute("SELECT * FROM " + table + " limit 10")
    #     rv = cur.fetchall()
    #     return str(rv)
from flask_mysqldb import MySQL

class Connect:

    def __init__(self, app):
        app.config["MYSQL_USER"] = "usuario"
        app.config["MYSQL_PASSWORD"] = "senha"
        app.config["MYSQL_DB"] = "saude"
        # Extra configs, optional:
        app.config["MYSQL_CURSORCLASS"] = "DictCursor"
        app.config["MYSQL_CUSTOM_OPTIONS"] = {"ssl": {"ca": "/path/to/ca-file"}}  # https://mysqlclient.readthedocs.io/user_guide.html#functions-and-attributes
        #variable of global for connection
        self.mysql = MySQL(app)


    def select(self):
        cur = self.mysql.connection.cursor()
        cur.execute("""SELECT * FROM users limit 10""")
        rv = cur.fetchall()
        return str(rv)

    def selectTable(self, table):
        cur = self.mysql.connection.cursor()
        cur.execute("SELECT * FROM " + table + " limit 10")
        rv = cur.fetchall()
        return str(rv)
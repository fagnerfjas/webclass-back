from flask import Flask
from app.db import Connect

app = Flask(__name__, static_folder='public')
from app import routes


database = Connect(app)




@app.route("/select")
def users():
    return database.selectTable('pacotes')
    



if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
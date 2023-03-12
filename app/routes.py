from app import app
from flask import render_template, redirect, url_for

@app.route('/')
@app.route('/index')
def index():    
    return render_template('index.html')

def guest(nome=""):
    if(nome == 'admin'):
        return redirect(url_for('admin', ))
    else:
        return "Bem vindo {}".format(nome)

def admin():
    return 'Administrador'

app.add_url_rule('/guest/', 'guest')
app.add_url_rule('/guest/<nome>', 'guest', guest)


app.add_url_rule('/admin/', 'admin', admin)
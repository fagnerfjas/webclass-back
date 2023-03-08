from flask import Flask

app = Flask(__name__)

@app.route('/mensage')
def hello():
	return 'Olá Mundão de Deus!'


app.run()
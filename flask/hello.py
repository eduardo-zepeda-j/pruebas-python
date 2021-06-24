from flask import Flask
from flask.globals import request

app  = Flask(__name__)

@app.route('/')
def hello_world():
    return "pagina principal"

@app.route('/pagina2')
def pagina2():
    return 'Hola: '

@app.route('/pagina3',methods=['POST'])
def pagina3():
    
    a = request.form.get('nombre')
    nombre= int(a)+int(1)
    return 'Hola '+ str(nombre)


if __name__ == '__main__':
    app.run()

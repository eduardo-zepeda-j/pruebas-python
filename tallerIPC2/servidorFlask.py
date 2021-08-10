from flask import Flask,request
from flask_cors import CORS


app = Flask(__name__)
cors = CORS(app,resources = {r'/*':{'origin':'*'}})

@app.route('/')
def index():
    contador = calculadora(10,24)
    return f'Hola Mundo {contador}'

def calculadora(num1,num2):
    return num1+num2

if __name__ == '__main__':
    app.run(debug=True)
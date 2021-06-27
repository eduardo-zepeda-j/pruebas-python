from flask import Flask,request

app = Flask(__name__)

@app.route('/')
def index():
    return 'hola mundo'

@app.route('/saluda')
def saluda():
    return 'otro mensaje'

@app.route('/params')
def params():
    param = request.args.get('params1','no contiene este parametro')
    param_dos = request.args.get('params2','no contiene este parametro')
    return 'El parametro es {}, {}'.format(param,param_dos)

if __name__ == '__main__':
    app.run(debug=True,port=8000)
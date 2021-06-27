from flask import Flask,request

app = Flask(__name__)

@app.route('/')
def index():
    return 'hola mundo'

@app.route('/params/')
@app.route('/params/<name>/')
@app.route('/params/<name>/<int:num>')
def params(name='un Valor Default',num='nada'):
    
    return 'El parametro es {} {}'.format(name,num)

if __name__ == '__main__':
    app.run(debug=True,port=8000)
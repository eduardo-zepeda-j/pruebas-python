from flask import Flask
from flask_cors import CORS

app = Flask(__name__)
cors = CORS(app,resources = {r'/*':{'origin':'*'}})

@app.route('/')
def index():
    return 'Hola Mundo'


if __name__ == '__main__':
    app.run(debug = True)
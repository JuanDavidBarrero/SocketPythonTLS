from flask import *
app = Flask(__name__)

@app.route('/')
def home():
   return '¡Hola Mundo!'

@app.route('/adios')
def adios():
   return 'Esto es una prueba'

if __name__ == '__main__':
   app.run(host='0.0.0.0', port=8000, debug=True)
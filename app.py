# Importamos librerias
from flask import Flask

#Creamos una variable app
app = Flask(__name__)

#definimos una funcion que imprime hola mundo
@app.route("/")
def hello():
    return "Hola Mundo."

#Creamos un condicional que corra nuestra funcion
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

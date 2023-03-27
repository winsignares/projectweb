#importo las librerias de flask
from flask import Flask, request
#importo las dependencias de trabajo
from config.db import app

@app.route("/")
def index():
    return "algo"

@app.route("/A", methods=['GET'])
def rutanueva():
    return "Andrey"

if __name__ == '__main__':
    app.run(debug=True)
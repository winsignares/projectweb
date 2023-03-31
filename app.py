#importo las librerias de flask
from flask import Flask, request, jsonify
#importo las dependencias de trabajo
from config.db import app

#importamos los modelos

from model.Users import Users, UsersSchema
from model.Taks import Taks, TaksSchema

user_schema = UsersSchema()
users_schema = UsersSchema(many=True)


@app.route("/")
def index():
    resultusers = Users.query.all()
    resultado = users_schema.dump(resultusers)
    return jsonify(resultado)

@app.route("/A", methods=['GET'])
def rutanueva():
    return "Andrey"

if __name__ == '__main__':
    app.run(debug=True)
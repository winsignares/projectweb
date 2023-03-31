#importo las librerias de flask
from flask import Flask, request, jsonify, json
#importo las dependencias de trabajo
from config.db import app, bd

#importamos los modelos

from model.Users import Users, UsersSchema
from model.Category import Category, CategorySchema
from model.Taks import Taks, TaksSchema


user_schema = UsersSchema()
users_schema = UsersSchema(many=True)

Category_schema = CategorySchema()
Categorys_schema = CategorySchema(many=True)

Taks_schema = TaksSchema()
Taks_schemas = TaksSchema(many=True)

@app.route("/")
def index():
    resultusers = Users.query.all()
    resultado = users_schema.dump(resultusers)
    return jsonify(resultado)

@app.route("/saveuser", methods=['POST'])
def rutanueva():
    fullname = request.json['fullname'] 
    email = request.json['email']
    newuser = Users(fullname, email)
    bd.session.add(newuser)
    bd.session.commit()     
    return "guardado"

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
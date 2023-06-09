#importo las librerias de flask
from flask import Flask, request, jsonify, json, render_template
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


@app.route("/", methods=['GET'])
def index():
    nombre= "Agregar Tarea"
    return render_template('taks.html', name = nombre)

@app.route("/usuario", methods=['GET'])
def usuario():
    nombre= "Agregar Usuario"
    return render_template('users.html',name = nombre)

@app.route("/Category", methods=['GET'])
def categoria():
    nombre= "Estamos en categoria"
    return render_template('category.html',name = nombre)


@app.route("/saveuser", methods=['POST'])
def rutanueva():
    fullname = request.json['fullname'] 
    email = request.json['email']
    newuser = Users(fullname, email)
    bd.session.add(newuser)
    bd.session.commit()     
    return "guardado"


@app.route("/eliminar", methods=['POST'])
def eliminaruser():    
    id = request.json['id'] 
    usuario = Users.query.get(id)    
    bd.session.delete(usuario)
    bd.session.commit()     
    return jsonify(user_schema.dump(usuario))

@app.route("/actualizar", methods=['POST'])
def actualizaruser():    
    id = request.json['id'] 
    fullname = request.json['fullname'] 
    email = request.json['email']
    usuario = Users.query.get(id)  
    usuario.fullname = fullname
    usuario.email = email
    bd.session.commit()     
    return "actualización exitosa"


@app.route('/dostablas', methods=['GET'])
def dostablas():
    results = bd.session.query(Users, Taks).join(Taks).all() 
    dato={}   
    i=0
    for users, taks in results:
        i+=1	       
        dato[i] = {
        'Nombre':users.fullname,
		'email':users.email,
		'NombreTarea':taks.nametak,                     
        }
        print(users.fullname, taks.nametak)
   
    #my_bytes = 'hello world'.encode('utf-8')

# ⛔️ TypeError: Object of type bytes is not JSON serializable
   
    return jsonify(dato)

@app.route('/unatabla', methods=['GET'])
def unatabla():
    results = bd.session.query(Users).all() 
    dato={}   
    i=0
    for users in results:
        i+=1	       
        dato[i] = {
        'Nombre':users.fullname,
		'email':users.email                   
        }
        print(users.fullname, users.email)
        
    return jsonify(dato)

@app.route('/todascategorias', methods=['GET'])
def todascategorias():
    results = bd.session.query(Category).all()
    dato={}
    i=0
    for category in results:
        i+=1
        dato[i]={
            'ID':category.id,
            'Nombre de categoria':category.namecategory
        }
        print(category.id, category.namecategory)
        
    return jsonify(dato)

@app.route('/trestablas',methods=['GET'])
def trestabla():
    results = bd.session.query(Users, Taks, Category). \
    select_from(Users).join(Taks).join(Category).all()
    dato={}   
    i=0
    for users, taks, category in results:
        i+=1
        dato[i] = {
        'Nombre':users.fullname,
		'tarea':taks.nametak,
		'categoria':category.namecategory,                     
        }       
        print(users.fullname, taks.nametak, category.namecategory)
    return jsonify(dato)

@app.route('/trestablaconfiltro', methods=['GET'])
def trestablaconfiltro():
    results = bd.session.query(Users.fullname, Users.email).join(Taks).join(Category). \
    filter(Users.id == 1).all()

    for result in results:
        print(result)
    return 'Dato'

# resultado = db.session.query(TblUsuarios, tblrolesusuarios).select_from(TblUsuarios.Cedula, TblUsuarios.full_name, TblUsuarios.telefono, TblUsuarios.cargo, tblrolesusuarios.rol).join(tblrolesusuarios).filter(tblrolesusuarios.roles== "personal").all()
   
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')

''' resultusers = Users.query.all()
    resultado = users_schema.dump(resultusers)
    return jsonify(resultado)'''
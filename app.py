from flask  import Flask,redirect,url_for,render_template,request
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from datetime import datetime

app = Flask(__name__)

app.config["MONGO_URI"] = "mongodb://localhost:27017/LucyMosqueraBD"
mongo = PyMongo(app)


@app.route('/')
def index():
    return redirect(url_for('registroPrestamos'))


@app.route('/registroPrestamos',methods=["GET","POST"])
def registroPrestamos():
    if request.method == 'POST':
        jsonvalue = request.form;
        id = jsonvalue['id']
        nombres = jsonvalue['nombres']
        monto = jsonvalue['monto']
        fecha_pagos = jsonvalue['fecha_pago']
        banco = jsonvalue['banco']
        meses = jsonvalue['meses']
        fecha_inicio = now = datetime.now()
        tiempo_credito = jsonvalue['tiempo_credito']
        print(fecha_inicio)
        #Insert
        idUsuario = mongo.db.user.insert({"_id":ObjectId(id),'nombres':nombres}).inserted_id
        #Query
        banco = mongo.db.Bancos.find_one({"nombre_banco":banco})
        idBanco = banco['_id']
        #Insert
        mongo.db.prestamos.insert({"tiempo_credito":tiempo_credito,"monto":monto,"id_usuario":idUsuario,"id_banco":idBanco})
    else:
        return render_template('FormPrestamo.html')



from types import NoneType
from flask import Flask, json, jsonify, request
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://postgres:<contraseña_db>@localhost:5432/tfg_project"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
cors = CORS(app)
db = SQLAlchemy(app)

from models.reservas import Reservas
from models.usuarios import Usuarios

array_usuarios = [Usuarios] * 50

@app.route('/api/v1.0/reservas')
def getMensaje ():
    reserv = Reservas.query.all()
    if (reserv != []):
        response = [
            {
                "nombre": res.nombre,
                "fecha": res.fecha,
                "email": res.email,
                "asistentes": res.asistentes,
                "id": res.id,
            } for res in reserv]
        print(response)
        return jsonify(response)
    else:
        return jsonify(False)

# Ruta de Inicio de sesión
@app.route('/api/v1.0/check_login', methods=['GET'])
def check_login ():
    # Extrae los datos del formulario del front y los almacena en variables
    email = request.args.get('email')
    contraseña = request.args.get('contraseña')
    # Almacena en una variable los datos obtenidos y filtrados por email (Solo puede existir un unico email, ya que es primary key)
    correo = Usuarios.query.filter_by(email = email).all()
    # Recuperamos la contraseña si hemos encontrado datos filtrados por email
    if (correo != []):
        for r in correo:
            results = r.contraseña
        # print (results)
        # Comprobamos que la contraseña coincida con la password almacenada para el correo, y poder iniciar sesion
        if (results == 'admin1234' and contraseña == 'admin1234'):
            res = 'admin1234'
            return jsonify(res)
        if (results == contraseña):
            return jsonify(True)
        else:
            return jsonify(False)

    else:
        return jsonify(False)

@app.route('/api/v1.0/register', methods=['GET'])
def register ():
    # Recuperamos los datos del formulario
    email = request.args.get('email')
    contraseña = request.args.get('contraseña')
    # Creamos un nuevo objeto a partir de los datos del formulario de tipo usuario
    new = Usuarios(email = email, contraseña = contraseña, role = False)
    # Comprobar que existe el email o no. En tal caso devolvemos un error
    correo = Usuarios.query.filter_by(email = email).all()
    # Serializamos
    if (correo != []):
        return jsonify(False)
    else:
    # Creacion de nuevo usuario
        db.session.add (new)
        db.session.commit()
        return jsonify(True)

@app.route('/api/v1.0/reserva_mesa', methods=['GET'])
def reserva_mesa ():
    # Recuperamos los datos del formulario
    nombre = request.args.get('nombre')
    fecha = request.args.get('fecha')
    email = request.args.get('email')
    asistentes = request.args.get('asistentes')
    # Creamos un nuevo objeto a partir de los datos del formulario de tipo reserva
    new_res = Reservas(nombre = nombre, fecha = fecha, email = email, asistentes = asistentes)
    # Creacion de nueva reserva
    db.session.add (new_res)
    db.session.commit()
    return jsonify(True)


if __name__ == '__main__':
    app.run(debug=True)
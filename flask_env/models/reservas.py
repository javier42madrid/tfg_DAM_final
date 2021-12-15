from server import db

class Reservas(db.Model):

    __tablename__ = 'Reservas'

    nombre = db.Column(db.String, nullable = False)
    fecha = db.Column(db.Date, nullable = False)
    email = db.Column(db.String, nullable = False)
    asistentes = db.Column(db.Integer, nullable = False)
    id = db.Column(db.Integer, nullable = False, primary_key = True)

    def __init__(self, nombre, fecha, email, asistentes):
        self.nombre = nombre
        self.fecha = fecha
        self.email = email
        self.asistentes = asistentes

    def serialize(self):
        return {
            "nombre": self.nombre,
            "fecha": self.fecha,
            "email": self.email,
            "asistentes": self.asistentes,
            "id": self.id
        }
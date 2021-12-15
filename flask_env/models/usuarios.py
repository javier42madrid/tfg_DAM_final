from server import db

class Usuarios(db.Model):

    __tablename__ = 'Usuarios'

    contraseña = db.Column(db.Integer, nullable = False)
    email = db.Column(db.Integer, nullable = False, primary_key=True)
    role = db.Column(db.Boolean, nullable = False)

    def __init__(self, email, contraseña, role):
        self.email = email
        self.contraseña = contraseña
        self.role = role

    def serialize(self):
        return {
            "email": self.email,
            "contraseña": self.contraseña,
            "role": self.role
        }
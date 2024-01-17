from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Ususario(db.Model):
  __tablename__ = "usuario"
  id = db.Column(db.Integer, primary_key=True)
  nombre = db.Column(db.String(50), nullable=False)
  apellido = db.Column(db.String(50), nullable=False)
  email = db.Column(db.String(50), unique=True)
  password = db.Column(db.String(20), nullable=False)

  def serialize_1(self):
    return {
      'id': self.id,
      'nombre': self.nombre,
      'apellido': self.apellido,
      'email': self.email
    }

  def serialize_2(self):
    return {
      'nombre': self.nombre
    }
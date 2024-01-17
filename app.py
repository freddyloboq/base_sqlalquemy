from flask import Flask, request, jsonify
from flask_migrate import Migrate
from models import db, Ususario

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///mibasededatos.db"

db.init_app(app)
migrate = Migrate(app, db)

@app.route("/", methods=['GET'])
def home():
  usuarios = Ususario.query.all()
  usuarios = list(map(lambda usuario: usuario.serialize_2(), usuarios))

  return jsonify({
    "data": usuarios,
    "status": 'success'
  }),200

@app.route("/usuario/<int:id>", methods=['GET'])
def get_user(id):
  usuario = Ususario.query.filter_by(id=id).first()
  if usuario is not None:
    return jsonify(usuario.serialize_1()), 200
  else:
    return jsonify({"error":"Usuario no encontrado"}),404


@app.route("/usuario/<int:id>", methods=['DELETE'])
def delete_user(id):
  usuario = Ususario.query.filter_by(id=id).first()
  if usuario is not None:
    db.session.delete(usuario)
    db.session.commit()
    return jsonify({
      "msg": "Usuario eliminado",
      "status": "Success"
    }), 203
  else:
    return jsonify({"error":"Usuario no encontrado"}),404

@app.route("/create", methods=["POST"])
def create():
  get_from_body = request.json.get("email")
  usuario = Ususario()
  usuario_existente = Ususario.query.filter_by(email=get_from_body).first()
  if usuario_existente is not None:
    return "El usuario ya existe"
  else:
    usuario.nombre = request.json.get("nombre")
    usuario.apellido = request.json.get("apellido")
    usuario.email = request.json.get("email")
    usuario.password = request.json.get("password")

    db.session.add(usuario)
    db.session.commit()

  return f"Se creo el usuario", 201


if __name__ == "__main__":
  app.run(host="localhost", port=5007, debug=True)
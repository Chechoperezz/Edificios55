from flask import Blueprint, request, jsonify
from models import db, Edificio, Usuario
from sqlalchemy.exc import IntegrityError
from marshmallow import ValidationError
from schemas import EdificioSchema, UsuarioSchema

api_bp = Blueprint('api', __name__, url_prefix='/api')

edificio_schema = EdificioSchema()
edificios_schema = EdificioSchema(many=True)

usuario_schema = UsuarioSchema()
usuarios_schema = UsuarioSchema(many=True)


@api_bp.route('/edificios', methods=['GET'])
def get_edificios():
    edificios = Edificio.query.all()
    return jsonify(edificios_schema.dump(edificios))


@api_bp.route('/edificios/<int:id>', methods=['GET'])
def get_edificio(id):
    edificio = Edificio.query.get_or_404(id)
    return jsonify(edificio_schema.dump(edificio))


@api_bp.route('/edificios', methods=['POST'])
def create_edificio():
    json_data = request.json
    if not json_data:
        return jsonify({"error": "No se proporcionaron datos de entrada"}), 400

    try:

        data = edificio_schema.load(json_data)
    except ValidationError as err:

        return jsonify(err.messages), 400

    try:
        new_edificio = Edificio(**data)
        db.session.add(new_edificio)
        db.session.commit()
        return jsonify(edificio_schema.dump(new_edificio)), 201
    except IntegrityError:
        db.session.rollback()
        return jsonify({"error": "Error de integridad de la base de datos (ej. duplicados de nombre)"}), 409
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500


@api_bp.route('/edificios/<int:id>', methods=['PUT'])
def update_edificio(id):
    edificio = Edificio.query.get_or_404(id)
    json_data = request.json
    if not json_data:
        return jsonify({"error": "No se proporcionaron datos de entrada"}), 400

    try:
        data = edificio_schema.load(json_data, partial=True)
    except ValidationError as err:
        return jsonify(err.messages), 400

    try:
        for key, value in data.items():
            setattr(edificio, key, value)

        db.session.commit()
        return jsonify(edificio_schema.dump(edificio))
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500


@api_bp.route('/edificios/<int:id>', methods=['DELETE'])
def delete_edificio(id):
    edificio = Edificio.query.get_or_404(id)
    db.session.delete(edificio)
    db.session.commit()
    return jsonify({"message": "Edificio eliminado correctamente"}), 200



@api_bp.route('/usuarios', methods=['GET'])
def get_usuarios():
    usuarios = Usuario.query.all()
    return jsonify(usuarios_schema.dump(usuarios))


@api_bp.route('/usuarios/<int:id>', methods=['GET'])
def get_usuario(id):
    usuario = Usuario.query.get_or_404(id)
    return jsonify(usuario_schema.dump(usuario))


@api_bp.route('/usuarios', methods=['POST'])
def create_usuario():
    json_data = request.json
    if not json_data:
        return jsonify({"error": "No se proporcionaron datos de entrada"}), 400

    try:
        data = usuario_schema.load(json_data)
    except ValidationError as err:
        return jsonify(err.messages), 400

    try:
        new_usuario = Usuario(**data)
        db.session.add(new_usuario)
        db.session.commit()
        return jsonify(usuario_schema.dump(new_usuario)), 201
    except IntegrityError:
        db.session.rollback()
        return jsonify({"error": "El email ya existe"}), 409
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500


@api_bp.route('/usuarios/<int:id>', methods=['PUT'])
def update_usuario(id):
    usuario = Usuario.query.get_or_404(id)
    json_data = request.json
    if not json_data:
        return jsonify({"error": "No se proporcionaron datos de entrada"}), 400

    try:
        data = usuario_schema.load(json_data, partial=True)
    except ValidationError as err:
        return jsonify(err.messages), 400

    try:
        for key, value in data.items():
            setattr(usuario, key, value)

        db.session.commit()
        return jsonify(usuario_schema.dump(usuario))
    except IntegrityError:
        db.session.rollback()
        return jsonify({"error": "El email ya existe"}), 409
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500


@api_bp.route('/usuarios/<int:id>', methods=['DELETE'])
def delete_usuario(id):
    usuario = Usuario.query.get_or_404(id)
    db.session.delete(usuario)
    db.session.commit()
    return jsonify({"message": "Usuario eliminado correctamente"}), 200
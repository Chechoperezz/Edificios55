from marshmallow import Schema, fields, validate


class EdificioSchema(Schema):
    nombre = fields.Str(required=True, validate=validate.Length(min=3, max=255))
    metrosCuadrados = fields.Float(required=True, validate=validate.Range(min=0.01))
    altura = fields.Float(required=True, validate=validate.Range(min=0.01))
    numPisos = fields.Int(required=True, validate=validate.Range(min=1))
    numApartamentos = fields.Int(required=True, validate=validate.Range(min=0))
    numOficinas = fields.Int(required=True, validate=validate.Range(min=0))
    nomParqueadero = fields.Str(validate=validate.Length(max=255), allow_none=True)
    numPiscinas = fields.Int(validate=validate.Range(min=0), allow_none=True)
    pais = fields.Str(required=True, validate=validate.Length(min=2, max=100))
    departamento = fields.Str(required=True, validate=validate.Length(min=2, max=100))
    ciudad = fields.Str(required=True, validate=validate.Length(min=2, max=100))
    tieneAscensor = fields.Bool(required=True)
    valorAdministracion = fields.Float(required=True, validate=validate.Range(min=0.0))
    tieneZonaSocial = fields.Bool(required=True)

class UsuarioSchema(Schema):
    nombre = fields.Str(required=True, validate=validate.Length(min=2, max=255))
    apellido = fields.Str(required=True, validate=validate.Length(min=2, max=255))
    email = fields.Email(required=True)
    password = fields.Str(required=True, validate=validate.Length(min=6))

    rol = fields.Str(validate=validate.OneOf(["admin", "usuario"]), load_default="usuario")
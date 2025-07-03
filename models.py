from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Edificio(db.Model):
    __tablename__ = 'edificios'
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(255), nullable=False)
    metrosCuadrados = db.Column(db.Numeric(10, 2), nullable=False)
    altura = db.Column(db.Numeric(10, 2), nullable=False)
    numPisos = db.Column(db.Integer, nullable=False)
    numApartamentos = db.Column(db.Integer, nullable=False)
    numOficinas = db.Column(db.Integer, nullable=False)
    nomParqueadero = db.Column(db.String(255))
    numPiscinas = db.Column(db.Integer)
    pais = db.Column(db.String(100), nullable=False)
    departamento = db.Column(db.String(100), nullable=False)
    ciudad = db.Column(db.String(100), nullable=False)
    tieneAscensor = db.Column(db.Boolean, nullable=False)
    valorAdministracion = db.Column(db.Numeric(10, 2), nullable=False)
    tieneZonaSocial = db.Column(db.Boolean, nullable=False)

    def to_dict(self):
        return {
            'id': self.id,
            'nombre': self.nombre,
            'metrosCuadrados': float(self.metrosCuadrados),
            'altura': float(self.altura),
            'numPisos': self.numPisos,
            'numApartamentos': self.numApartamentos,
            'numOficinas': self.numOficinas,
            'nomParqueadero': self.nomParqueadero,
            'numPiscinas': self.numPiscinas,
            'pais': self.pais,
            'departamento': self.departamento,
            'ciudad': self.ciudad,
            'tieneAscensor': self.tieneAscensor,
            'valorAdministracion': float(self.valorAdministracion),
            'tieneZonaSocial': self.tieneZonaSocial
        }

class Usuario(db.Model):
    __tablename__ = 'usuarios'
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(255), nullable=False)
    apellido = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(255), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)
    rol = db.Column(db.String(50), default='usuario')

    def to_dict(self):
        return {
            'id': self.id,
            'nombre': self.nombre,
            'apellido': self.apellido,
            'email': self.email,
            'rol': self.rol
        }
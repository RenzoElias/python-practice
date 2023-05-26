from datetime import datetime
from app import db
from sqlalchemy.sql import func

# Base de datos Holding - db_usuarios
class Notificacion(db.Model):
    __bind_key__ = "db_usuarios"
    __tablename__ = "notificacion"
    idnotificacion = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(255))
    estado = db.Column(db.Integer)
    idplataforma = db.Column(db.Integer)
    descripcion = db.Column(db.String(8000))
    correo_salida = db.Column(db.String(255))

class NotificacionDetalle(db.Model):
    __bind_key__ = "db_usuarios"
    __tablename__ = "notificacion_detalle"
    idnotificacion_detalle = db.Column(db.Integer, primary_key=True)
    idnotificacion = db.Column(db.Integer, db.ForeignKey("notificacion.idnotificacion"))
    cuenta_alternativa = db.Column(db.String(255))
    fecha_registro = db.Column(db.DateTime, default=datetime.now)
    tipo_envio = db.Column(db.Integer)
    estado = db.Column(db.Integer)





# Base de datos Global Red Salud - global_rs
class Asegurado(db.Model):
    __tablename__ = "asegurado"
    __table_args__ = {"extend_existing": True}
    idasegurado = db.Column(db.Integer, primary_key=True)
    apellido_paterno = db.Column(db.String(255), default="")
    apellido_materno = db.Column(db.String(255), default="")
    nombre1 = db.Column(db.String(255), default="")
    nombre2 = db.Column(db.String(255), default="")
    tipo_documento = db.Column(db.Integer)
    nro_documento = db.Column(db.String(20))
    telefono = db.Column(db.String(10))
    correo = db.Column(db.String(255))
    genero = db.Column(db.Integer)
    direccion = db.Column(db.String(255))
    ubigeo = db.Column(db.String(6))
    fecha_nacimiento = db.Column(db.Date())
    co_pais = db.Column(db.String(3), default="PER")


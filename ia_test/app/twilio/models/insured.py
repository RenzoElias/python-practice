from app import db
from sqlalchemy.sql import func


class Insured(db.Model):
    __tablename__ = "asegurado_suscripcion"

    idasegurado_suscripcion = db.Column(db.Integer, primary_key=True)

    idtipodocumento = db.Column(db.Integer)
    nro_documento = db.Column(db.String(20))

    apellido_paterno = db.Column(db.String(255))
    apellido_materno = db.Column(db.String(255))
    nombre1 = db.Column(db.String(255))
    nombre2 = db.Column(db.String(255))

    fecha_nacimiento = db.Column(db.Date())
    correo = db.Column(db.String(255))
    sexo = db.Column(db.String(255))
    ubigeo = db.Column(db.String(6))
    direccion = db.Column(db.String(255))
    direccion = db.Column(db.String(255))
    telefono = db.Column(db.String(10))

    tipo = db.Column(db.Integer)
    idcontratante = db.Column(db.String(20))
    declaracion_jurada = db.Column(db.String(1))

    pregunta1 = db.Column(db.String(1))
    pregunta2 = db.Column(db.String(1))
    pregunta3 = db.Column(db.String(1))
    pregunta4 = db.Column(db.String(1))
    pregunta5 = db.Column(db.String(1))
    pregunta6 = db.Column(db.String(1))
    tc_datos = db.Column(db.String(1))
    tc_comunicaciones = db.Column(db.String(1))
    tc_pago = db.Column(db.String(1))

    estado = db.Column(db.Integer)
    tipo_procesamiento = db.Column(db.Integer)
    fecha_registro = db.Column(db.DateTime(), server_default=func.now())
    idplan = db.Column(db.Integer)
    idcliente = db.Column(db.Integer)
    frecuencia_pago = db.Column(db.Integer)
    tipo_afiliacion = db.Column(db.Integer)
    importe = db.Column(db.Numeric())
    estado_pago = db.Column(db.Integer)
    idplataforma = db.Column(db.Integer)
    tipo_pago = db.Column(db.Integer)
    nacionalidad = db.Column(db.String(3))
    idparentesco = db.Column(db.Integer)
    customerid = db.Column(db.String(255))
    suscripcionid = db.Column(db.String(255))
    orderid = db.Column(db.String(255))
    fecha_creacion = db.Column(db.DateTime())
    fecha_transaccion = db.Column(db.DateTime())
    tipo_suscripcion = db.Column(db.Integer)
    comentario = db.Column(db.Text(length=3000))
    dcto_importe = db.Column(db.Numeric())
    iddescuento = db.Column(db.Integer)
    idpasarela = db.Column(db.Integer)
    transactionid = db.Column(db.String(255))
    ticket_number = db.Column(db.String(255))
    idcombo = db.Column(db.Integer)

    def full_name(self):
        if self.idtipodocumento == 1:
            return f"{self.nombre1} {self.nombre2} {self.apellido_paterno} {self.apellido_materno}".strip().title()
        elif self.idtipodocumento == 8:
            return f"{self.apellido_paterno}".strip().title()

    def get_gender(self):
        if self.idtipodocumento == 1:
            return 'Masculino' if self.sexo == '1' else 'Femenino'
        elif self.idtipodocumento == 8:
            return ''

    def __str__(self):
        full_name = f"{self.apellido_paterno or ''} {self.apellido_materno or ''} {self.nombre1 or ''} {self.nombre2 or ''}".strip().title()
        return full_name


class Insured_transaction(db.Model):
    __tablename__ = "asegurado_transaccion"
    idasegurado_transaccion=db.Column(db.Integer, primary_key=True)
    idasegurado_suscripcion= db.Column(db.Integer)
    customerid= db.Column(db.String(255))
    ticket_number=db.Column(db.String(255))
    transaction_id=db.Column(db.String(255))
    transaction_reference=db.Column(db.String(255))
    suscripcionid=db.Column(db.String(255))
    orderid=db.Column(db.String(255))
    idpasarela=db.Column(db.Integer)
    estado_pago= db.Column(db.Integer)
    idcertificado= db.Column(db.Integer)
    importe=db.Column(db.Integer)
    fecha_registro=db.Column(db.DateTime(), server_default=func.now())
    idcobro=db.Column(db.Integer)
class Parentesco(db.Model):
    __tablename__ = "parentesco"
    idparentesco=db.Column(db.Integer, primary_key=True)
    descripcion= db.Column(db.String(255))
    estado=db.Column(db.Integer)

    fecha_reg=db.Column(db.DateTime(), server_default=func.now())

class Asegurado_transaccion_det(db.Model):
    __tablename__ = "asegurado_transaccion_det"
    idasegurado_transaccion_det=db.Column(db.Integer, primary_key=True)
    idasegurado_transaccion=db.Column(db.Integer)
    idcertificado=db.Column(db.Integer)
    fecha_reg=db.Column(db.DateTime(), server_default=func.now())
    idcobro=db.Column(db.Integer)
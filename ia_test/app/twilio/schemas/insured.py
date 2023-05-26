from app import ma

class InsuredScheme(ma.Schema):
    class Meta:
        fields = (
            "idasegurado_suscripcion",
            "idtipodocumento",
            "nro_documento",
            "apellido_paterno",
            "apellido_materno",
            "nombre1",
            "nombre2",
            "fecha_nacimiento",
            "correo",
            "sexo",
            "ubigeo",
            "direccion",
            "direccion",
            "telefono",
            "tipo",
            "idcontratante",
            "declaracion_jurada",
            "pregunta1",
            "pregunta2",
            "pregunta3",
            "tc_datos",
            "tc_comunicaciones",
            "tc_pago",
            "estado",
            "tipo_procesamiento",
            "fecha_registro",
            "idplan",
            "frecuencia_pago",
            "tipo_afiliacion",
            "importe",
            "estado_pago",
            "idplataforma",
            "tipo_pago",
            "nacionalidad",
            "idparentesco",
            "customerid",
            "suscripcionid",
            "orderid",
            "fecha_creacion",
            "fecha_transaccion",
            "tipo_suscripcion",
            "comentario",
            "idpasarela",
            "dcto_importe",
            "transactionid",
            "ticket_number",
            "idcombo"
        )

insured_schema = InsuredScheme()
insureds_schema = InsuredScheme(many=True)


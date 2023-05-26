from app import ma

class SesionSchema(ma.Schema):
    class Meta:
        fields = (
            "idsesion",
            "token",
            "idusuario",
            "flg_tipo",
            "datetime"
        )

sesion_schema = SesionSchema()
sesion_schemas = SesionSchema(many=True)
from app.twilio.models.insured import Insured
from app.twilio.schemas.insured import insured_schema, insureds_schema


def get_insureds():
    insureds = Insured.query.all()
    data = insureds_schema.dump(insureds)
    return data

def get_insured_by_id(idasegurado_suscripcion: int):
    insured_by_id = Insured.query.filter(Insured.idasegurado_suscripcion == idasegurado_suscripcion).first()
    data = insured_schema.dump(insured_by_id)
    if data:
        return {"success": True, "result": data}
    else:
        return {"success": True, "result": data, "empty": True}

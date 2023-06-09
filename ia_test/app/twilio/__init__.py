from flask import Blueprint, request, jsonify
from app.twilio.controllers import twilio 

bp = Blueprint('twilio', __name__, template_folder='templates')

@bp.route('/')
@bp.route('/home')
def home():
    return jsonify({"response": "Module Twilio API"})

@bp.route('/callback', methods=['POST'])
def callback():
    data = twilio.getCallBack()
    return jsonify(data)

# @bp.route('/registrarcombo/<string:nro_documento>/<int:tipo_proc>/<int:idcont>')
# def get_asegurado_combo(nro_documento, tipo_proc, idcont):
#     data = registercombo.get_asegurados_combo(nro_documento, tipo_proc, idcont)
#     return jsonify(data)




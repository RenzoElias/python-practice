from flask import Blueprint, request, jsonify
# from app.plataforma.controllers import cliente, historia_clinica, login,usuario, horario, siniestro

bp = Blueprint('twilio', __name__, template_folder='templates')

@bp.route('/')
@bp.route('/home')
def home():
    return jsonify({"response": "Red Salud ecommerce API"})

@bp.route('/callback', methods=['POST','GET'])
def callback():
    transcription = request.form.get('TranscriptionText')
    # Realizar acciones con la transcripción de la respuesta
    return 'OK'

    # data = insured.get_insureds()
    # return jsonify(data)

# @bp.route('/registrarcombo/<string:nro_documento>/<int:tipo_proc>/<int:idcont>')
# def get_asegurado_combo(nro_documento, tipo_proc, idcont):
#     data = registercombo.get_asegurados_combo(nro_documento, tipo_proc, idcont)
#     return jsonify(data)
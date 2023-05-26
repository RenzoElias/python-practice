from sqlalchemy.sql import text
from app import db

# Recuerda instalar las bibliotecas necesarias, como requests, google-cloud-speech
# from google.cloud import speech

# import requests

# def descargar_audio(recording_url, archivo_salida):
#     response = requests.get(recording_url)
#     with open(archivo_salida, 'wb') as archivo:
#         archivo.write(response.content)


# def convertir_audio_a_texto(archivo_audio):
#     cliente_speech = speech.SpeechClient()

#     with open(archivo_audio, 'rb') as archivo:
#         contenido_audio = archivo.read()

#     audio = speech.RecognitionAudio(content=contenido_audio)
#     config = speech.RecognitionConfig(
#         encoding=speech.RecognitionConfig.AudioEncoding.LINEAR16,
#         sample_rate_hertz=16000,
#         language_code="es-ES",
#     )

#     respuesta = cliente_speech.recognize(config=config, audio=audio)

#     texto_transcrito = ""
#     for resultado in respuesta.results:
#         texto_transcrito += resultado.alternatives[0].transcript

#     return texto_transcrito


def procesar_respuesta(respuesta_persona):
    # Utiliza tu biblioteca de NLP para procesar la respuesta
    # y generar una respuesta de la IA
    respuesta_ai = "Respuesta generada por la IA"
    return respuesta_ai




def emailCopy(noti):
	correos=''
	queryto = text(f"call db_usuarios.sp_notificar({noti})")
	response = db.session.execute(queryto).all()
	if response:
		number_emails = len(response)
		for i in response:
			if number_emails !=1:
				correos+=i.correo+','
			else:
				correos+=i.correo
			number_emails=number_emails-1
		print(correos)
		return correos
	else:
		return False
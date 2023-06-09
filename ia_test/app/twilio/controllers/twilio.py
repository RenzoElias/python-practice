from flask import request, copy_current_request_context
from datetime import date, datetime

import os
from twilio.rest import Client
from twilio.twiml.voice_response import Gather, VoiceResponse, Dial

# Configurar las credenciales de Twilio
account_sid = os.getenv('ACCOUNT_SID')
auth_token = os.getenv('AUTH_TOKEN')
client = Client(account_sid, auth_token)

# import openai
# openai.api_key = 'TU_API_KEY'


def getCallBack2():
    try:
        
        body= request.json
        data = None
        
        # Procesar la notificación de Twilio
        call_sid = request.form['CallSid']
        call_status = request.form['CallStatus']
        speech_result = request.form['SpeechResult']
        
        # Realizar acciones según la respuesta de la persona
        if speech_result == 'respuesta 1':
            respuesta = 'La respuesta 1 seleccionada. ¿Qué más puedo hacer por ti?'
        elif speech_result == 'respuesta 2':
            respuesta = 'La respuesta 2 seleccionada. ¿En qué más puedo ayudarte?'
        else:
            respuesta = 'No comprendí tu respuesta. Por favor, intenta de nuevo.'
        
        # Iniciar la respuesta de la IA
        # ...
        
        # Enviar la respuesta de la IA a la llamada
        call = client.calls(call_sid).fetch()
        client.calls(call_sid).update(
            twiml=f'<Response><Say>{respuesta}</Say></Response>'
        )
        
        return {
            "success": True,
            "data": data
        }
    except Exception as e:
        print(e)
        return {"success": False}

def getCallBack1():
    try:
        
        body= request.json
        data = None
        
        # Procesar la notificación de Twilio
        call_sid = request.form['CallSid']
        call_status = request.form['CallStatus']
        
        # Obtener la transcripción de la respuesta
        transcription = request.form['TranscriptionText']
        
        # Realizar acciones según la transcripción
        
        return {
            "success": True,
            "data": data
        }
    except Exception as e:
        print(e)
        return {"success": False}

def getCallBack():
    try:
        # account_sid = os.getenv('ACCOUNT_SID')
        # auth_token = os.getenv('AUTH_TOKEN')
        # client = Client(account_sid, auth_token)
        # body= request.json
        data = None
        
        initial = "Hola mundo"
        
        # breakpoint()
        
        call = client.calls.create(
                        twiml='<Response><Say>Hola Mundo</Say></Response>',
                        # twiml=f'<Response><Say>{initial}</Say></Response>',
                        # url='http://demo.twilio.com/docs/voice.xml',
                        # to='+51934868395',
                        to='+51929202772',
                        # from_='+51929202772'
                        from_='+13613487918'
                    )
        
        # breakpoint()
        
        print(call)
        print(call.sid)
        
        
        return {
            "success": True,
            "data": call
        }
    except Exception as e:
        print(e)
        return {"success": False}

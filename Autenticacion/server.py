# -*- coding: utf-8 -*-
"""
Created on Mon Oct 17 07:30:45 2022

@author: Diana Marin
"""

from flask import Flask
import os
from twilio.rest import Client
from flask import request
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

app=Flask(__name__) #Instanciando una clase de tipo Flask

@app.route('/')
def inicio():
    respuesta=os.environ.get("Prueba")
    return respuesta


@app.route('/sms')
def sms():
    try:
    
        account_sid = os.environ['TWILIO_ACCOUNT_SID']
        auth_token = os.environ['TWILIO_AUTH_TOKEN']
        client = Client(account_sid, auth_token)
        contenido=request.args.get("mensaje")
        destino=request.args.get("telefono")
        message = client.messages \
                        .create(
                             body=contenido,
                             from_='+15017122661',
                             to=destino
                         )
        
        print(message.sid)
        return "Enviado correctamente"
    except Exception as e:
        return "Error enviando el mensaje"


@app.route('/e-mail')
def mail():
    
    destino=request.args.get("correo_destino")
    asunto=request.args.get("asunto")
    mensaje=request.args.get("contenido")
    
    
    message = Mail(
        from_email='progwebmintic@gmail.com',
        to_emails=destino,
        subject=asunto,
        html_content=mensaje)
    try:
        sg = SendGridAPIClient(os.environ.get('SENDGRID_API_KEY'))
        response = sg.send(message)
        print(response.status_code)
        print(response.body)
        print(response.headers)
        return "Correo enviado exitosamente!!"
    except Exception as e:
        print(e.message)
        return "Error!, el correo no fue enviado"
    
    
    
    
    
    

if __name__=='__main__':
    app.run()
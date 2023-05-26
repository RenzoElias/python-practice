import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
# from email.message import EmailMessage
from app.config import FLASK_ENV, EMAIL_SENDER, EMAIL_SMTP, EMAIL_PORT, EMAIL_USER, EMAIL_PASS
from app.plataforma.utils import methods



def load_file(message, files):
    try:
        for file_pdf in files:
            if file_pdf.endswith('.pdf'):
                with open(file_pdf, 'rb') as fil:
                    part = MIMEApplication(fil.read(), Name=file_pdf)
                part.add_header('Content-Disposition', 'attachment', filename=file_pdf)
                message.attach(part)
        return True
    except Exception as e:
        print(e)
        return False



def sendCorreoAdjunto(cuerpo, subject, correo, files=[], copy_email=''):
    email_subject = subject
    # sender_email_address = "reservasredsalud@red-salud.com"
    sender_email_address = f"SumaSalud <{EMAIL_SENDER}>"
    receiver_email_address = correo
    copy_email_address=copy_email
    # copy_email_address='renzoeliasdelacalle@gmail.com'
    # email_smtp = "email-smtp.us-east-1.amazonaws.com"

    # Create an email message object
    message = MIMEMultipart()
    # Configure email headers

    message['Subject'] = email_subject
    message['From'] = sender_email_address
    message['To'] = receiver_email_address
    
    if FLASK_ENV == "production":
        message['Bcc']=copy_email_address
        # message['Bcc']='renzo.456.456@gmail.com'

    message.attach(MIMEText(cuerpo, 'html'))
    load_file(message, files)
    respuesta=''
    try:
        # Set smtp server and port
        server = smtplib.SMTP(EMAIL_SMTP, EMAIL_PORT)
        # server = smtplib.SMTP(email_smtp, '587')

        # Identify this client to the SMTP server
        server.ehlo()

        # Secure the SMTP connection
        server.starttls()

        # Login to email account
        # server.login('AKIA2PRSJRH66HRTLLES', 'BO1cymlPAsO8Wn80PNY46rMuWokedC307o7KwCoMIVJE')
        server.login(EMAIL_USER, EMAIL_PASS)

        # Send email
        server.send_message(message)

        # Close connection to server
        methods.remove_pdf(files)
        server.quit()
        respuesta="success"
    except Exception as e:
        print(e)
        respuesta="Failed"
    return respuesta










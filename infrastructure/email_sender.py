#Librerias
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from config.settings import EMAIL_USER, EMAIL_PASSWORD, SMTP_SERVER, SMTP_PORT
from domain.email_data import EmailData

#Creacion de la clase EmailSender
class EmailSender:

    #Constructor
    def send_email(self, email_data: EmailData, body: str):
        message = MIMEMultipart()
        message["From"] = EMAIL_USER
        message["To"] = email_data.recipient_email
        message["Subject"] = email_data.subject

        message.attach(MIMEText(body, "plain"))

        #Validacion si el email se envia o no
        try:
            with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
                server.starttls()
                server.login(EMAIL_USER, EMAIL_PASSWORD)
                server.send_message(message)

        except smtplib.SMTPException as error:
            raise RuntimeError("Error en el envio via SMTP") from error

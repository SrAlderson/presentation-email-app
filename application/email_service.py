#Librerias
from infrastructure.email_sender import EmailSender
from domain.email_data import EmailData

#Creacion de la clase EmailService
class EmailService:

    #constructor del servicio
    def __init__(self):
        self.sender = EmailSender()

    #Metodo del cuerpo del correo
    def build_email_body(self, email_data: EmailData):
        student_list = "\r\n".join(
          f"- {student.full_name.strip()}"  # limpio espacios extras
          for student in email_data.students
        )

        # Texto del email sin indentación extra
        return f"""Buen día,

Cordial saludo {email_data.recipient_name},

Por medio del presente correo nos permitimos realizar la presentación
de los estudiantes del programa {email_data.program},
quienes cursan la asignatura {email_data.course}.

Listado de estudiantes:
{student_list}

Adicionalmente esta es la URL donde esta el proyecto. 
URL: https://github.com/SrAlderson/presentation-email-app

Cordialmente,
Estudiantes del programa {email_data.program}"""

    #Metodo del envio del correo
    def send(self, email_data: EmailData):
        body = self.build_email_body(email_data)
        self.sender.send_email(email_data, body)

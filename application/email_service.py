#Librerias
from infrastructure.email_sender import EmailSender
from domain.email_data import EmailData

#Creacion de la clase EmailService
class EmailService:

    #constructor del servicio
    def __init__(self):
        self.sender = EmailSender()

    def build_email_body_plain(self, email_data: EmailData):
        student_list = "\n".join(
            f"- {student.full_name}"
            for student in email_data.students
        )

        return f"""
    Buen día,

    Cordial saludo {email_data.recipient_name},

    Por medio del presente correo nos permitimos realizar la presentación
    de los estudiantes del programa {email_data.program},
    quienes cursan la asignatura {email_data.course}.

    Listado de estudiantes:
    {student_list}

    Cordialmente,
    Estudiantes del programa {email_data.program}
    """.strip()

    #Metodo del cuerpo del correo
    def build_email_body_html(self, email_data: EmailData):
        student_list = "".join(
            f"<li>{student.full_name}</li>"
            for student in email_data.students
        )

        return f"""
        <html>
          <body style="font-family: Arial, sans-serif; color: #1f2937; line-height: 1.6;">
            <p>Buen día,</p>

            <p>
              Cordial saludo <strong>{email_data.recipient_name}</strong>,
            </p>

            <p>
              Por medio del presente correo nos permitimos realizar la presentación
              de los estudiantes del programa <strong>{email_data.program}</strong>,
              quienes cursan la asignatura <strong>{email_data.course}</strong>.
            </p>

            <p><strong>Listado de estudiantes:</strong></p>

            <ul>
              {student_list}
            </ul>

            <p>
              Cordialmente,<br>
              <strong>Estudiantes del programa {email_data.program}</strong>
            </p>
          </body>
        </html>
        """

    def send(self, email_data: EmailData):
        plain_body = self.build_email_body_plain(email_data)
        html_body = self.build_email_body_html(email_data)

        self.sender.send_email(
            to_email=email_data.recipient_email,
            subject=email_data.subject,
            plain_body=plain_body,
            html_body=html_body
        )


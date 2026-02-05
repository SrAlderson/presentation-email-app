#librerias
from flask import Blueprint, render_template, request, flash, redirect,url_for
from application.email_service import EmailService
from domain.student import Student
from domain.email_data import EmailData

email_bp = Blueprint("email", __name__)

#Controlador
@email_bp.route("/", methods=["GET", "POST"])
def send_email():

    if request.method == "POST":

        #Campos obligatorios
        required_fields = [
            "recipient_email", "recipient_name", "subject",
            "course", "program", "students"
        ]

        #Validacion de los campos
        for field in required_fields:
            if not request.form.get(field):
                flash("Todos los campos son obligatorios")
                return redirect(url_for("email.send_email"))

        #Construccion de lista de estudiantes
        students = [
            Student(name.strip())
            for name in request.form["students"].splitlines()
            if name.strip()
        ]

        if not students:
            flash("Debe ingresar al menos un estudiante", "error")
            return redirect(url_for("email.send_email"))

        #Crea todo el objeto email data
        email_data = EmailData(
            recipient_email=request.form["recipient_email"],
            recipient_name=request.form["recipient_name"],
            subject=request.form["subject"],
            course=request.form["course"],
            program=request.form["program"],
            students=students
        )

        #Validar el envio de email
        try:
            EmailService().send(email_data)
            flash("Correo enviado correctamente", "success")
        except Exception:
            flash("Ocurrió un error al enviar el correo", "error")

        return redirect(url_for("email.send_email"))

    return render_template("form.html")

# Librerías
from flask import Blueprint, render_template, request, flash, redirect, url_for
import re

from application.email_service import EmailService
from domain.student import Student
from domain.email_data import EmailData

email_bp = Blueprint("email", __name__)

@email_bp.route("/", methods=["GET", "POST"])
def send_email():

    if request.method == "POST":

        recipient_email = request.form.get("recipient_email", "").strip()
        recipient_name = request.form.get("recipient_name", "").strip()
        subject = request.form.get("subject", "").strip()
        course = request.form.get("course", "").strip()
        program = request.form.get("program", "").strip()
        students_raw = request.form.get("students", "").strip()

        # Validación campos obligatorios
        if not all([
            recipient_email, recipient_name, subject,
            course, program, students_raw
        ]):
            flash("Todos los campos son obligatorios", "error")
            return redirect(url_for("email.send_email"))

        # Validación formato correo
        if not re.match(r"[^@]+@[^@]+\.[^@]+", recipient_email):
            flash("El correo electrónico no es válido", "error")
            return redirect(url_for("email.send_email"))

        # Construcción de lista de estudiantes
        students = [
            Student(name.strip())
            for name in students_raw.splitlines()
            if name.strip()
        ]

        if len(students) == 0:
            flash("Debe ingresar al menos un estudiante", "error")
            return redirect(url_for("email.send_email"))

        # Crear objeto de dominio EmailData
        email_data = EmailData(
            recipient_email=recipient_email,
            recipient_name=recipient_name,
            subject=subject,
            course=course,
            program=program,
            students=students
        )

        # Envío del correo
        try:
            EmailService().send(email_data)
            flash("Correo enviado correctamente", "success")
        except Exception as e:
            print(f"Error enviando correo: {e}")
            flash("Ocurrió un error al enviar el correo", "error")

        return redirect(url_for("email.send_email"))

    return render_template("form.html")

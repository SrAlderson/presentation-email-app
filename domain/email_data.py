#Librerias
from domain.student import Student
from typing import List
#Creacion de la clase email data
class EmailData:

    #Construtctor
    def __init__(self, recipient_email: str, recipient_name: str, subject: str, course: str, program: str, students: List[Student]):
        
        #Datos a solicitar
        self.recipient_email = recipient_email
        self.recipient_name = recipient_name
        self.subject = subject
        self.course = course
        self.program = program
        self.students = students

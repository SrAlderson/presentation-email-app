#Librerias
import os
from dotenv import load_dotenv

#Lee archivo .env para cargar las variables
load_dotenv()

#Variables de entorno
EMAIL_USER = os.getenv("EMAIL_USER")
EMAIL_PASSWORD = os.getenv("EMAIL_PASSWORD")
SMTP_SERVER = os.getenv("SMTP_SERVER", "smtp.gmail.com")
SMTP_PORT = int(os.getenv("SMTP_PORT", 587))

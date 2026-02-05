#Librerias

from flask import Flask
from presentation.controllers.email_controller import email_bp

#Creacion de la instancia
app = Flask(__name__)

#Clave secreta de la aplicacion
app.secret_key = "dev_key"

#Controlador de la aplicacion
app.register_blueprint(email_bp)

#Ejecucion del archivo
if __name__ == "__main__":
    app.run(debug=True)

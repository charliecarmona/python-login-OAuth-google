# -*- coding: utf-8 -*-
import os #modulo nos permiten manipular la estructura de directorios dependientes del sistema operativo

from flask import Flask, jsonify #importe de jsonifi obtenido de flask para emitir jason
from proveedor import GoogleLogin #importe de del paquete del provedor y uso del proveedor

#Definición de variables de entorno, usa aqui tus API keys.
#Asignacion de variables con valor proporcionado por google en su registro id_cliente y secret_cliente
os.environ["GOOGLE_LOGIN_CLIENT_ID"] = "364672633912-hbhtatjd9kbkbeaocn0902pivum4t0cd.apps.googleusercontent.com"
os.environ["GOOGLE_LOGIN_CLIENT_SECRET"] = "b_HGPbqiY-gBHSCBuS38fVau"


# Configuracion de la app
app = Flask(__name__)
app.config.update(
  SECRET_KEY="x34sdfm34",
)


"""
Se crea un tupla de llave-valor que luego se itera en el diccionario app.config donde se alamcena
el par de tokens del proveedor.

"""
for config in (
  "GOOGLE_LOGIN_CLIENT_ID",
  "GOOGLE_LOGIN_CLIENT_SECRET"

):app.config[config] = os.environ[config]


# Se instancia la clase con las configuraciones repectivas del provedor
google_login = GoogleLogin(app)



# Definicion de la ruta raiz

"""
En la ruta raiz se retorna un HTML con enlaze a las 3 opciones de login, mateniendo el minimalismo, se usa la
funcion 'format' para hacer render de las urls de autorizacion en su orden definición en los parámetros de esta
y la aparición de las llaves en los hrefs.
"""
@app.route("/")
def index():
  return """
<html>
<a href="{}">Python Login con con cuenta de Google </a>
""".format(google_login.authorization_url())

"""
Luego que alguna opcion de login es selecionada se responde con una fallo o con exito
para el cual se responde con el JSON retornado por el API de cada proveedor utilizando la funcion 'jsonify'

Las funciones a continacion son implementaciones de la funciones login_success y login_failure definidas en la
clase base OAuth2Login con esto podemos cambiar el comportamiento en la respuesta dependiendo de cada proveedor
almacenarlo en una base de datos y mostrar un perfil foto etc Pero para el objetivo de esta practica solo se muestra
la respuesta exitosa con la informacion del usuario (almacenada en la variable profile) en formato JSON tal cual como
lo envia el API del proveedor

"""
@google_login.login_success
def login_success(token, profile):
  return jsonify(token=token, profile=profile)

"""
Metetodo implementado si no hay error obtendra informacion del usuario
y del token y los emitira en un JSON en la pantalla
"""

@google_login.login_failure
def login_failure(e):
  return jsonify(error=str(e))

"""
Metetodo que entrara en uso si hay errores de cualquier tipo
"""



if __name__ == "__main__":
  app.run(host="0.0.0.0", debug=True)
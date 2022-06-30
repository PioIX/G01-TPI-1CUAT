from flask import Flask, render_template
from random import randint
import sqlite3

app = Flask(__name__)

### crearBaseDeDatos():
#  Crea una base de datos para almacenar una tabla
#  "jugadores":
#    Los campos serían:
#      nombre (primary key)
#      puntos (respuestas correctas)
#      tiempo (tiempo de juego)
def crearBaseDeDatos():
  conn = sqlite3.connect('database.db')

  q = """
        CREATE TABLE IF NOT EXISTS jugadores 
        (
          nombre     TEXT NOT NULL PRIMARY KEY,
          puntos     INTEGER,
          tiempo     TEXT
        );
      """

  conn.execute(q)

  conn.close()
  
def girarRuleta():
  num = randint(1, 4)
  if num == 1:
    ods = "Fin de la pobreza"
  elif num == 2:
    ods = "Hambre cero"
  elif num == 3:
    ods = "Salud y bienestar"
  elif num == 4:
    ods = "Educación de calidad"
  return [num, f"El ODS seleccionado es: ODS {num}: '{ods}'"]

@app.route('/')
def index():
  crearBaseDeDatos()
  return render_template('index.html')

@app.route('/ingresa_nombre', methods=['GET', 'POST'])
def ingresarDatos():
  return render_template('usuario.html')

@app.route('/ruleta')
def ruleta():
  return render_template('ruleta.html', res = girarRuleta())

@app.route('/pregunta')
def pregunta():
  return render_template('pregunta.html')

@app.route('/perdiste')
def perder():
  return render_template('perdiste.html')

@app.route('/puntajes')
def tablaPuntajes():
  return render_template('leaderboard.html')

app.run(host='0.0.0.0', port=81)
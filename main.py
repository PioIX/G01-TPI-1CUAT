from flask import Flask, render_template, request
from random import randint
import sqlite3
import time

app = Flask(__name__)

### crearBaseDeDatos():
#  Crea una base de datos para almacenar dos tablas
#  "jugadores":
#    Los campos serían:
#      nombre (primary key)
#      puntos (respuestas correctas)
#      tiempo (tiempo de juego)
#  "preguntas":
#    Los campos serían:
#      id (primary key)
#      pregunta (la pregunta que se imprime en pantalla)
#      respuesta (la respuesta correcta)
#      inco_1 (opcion incorrecta 1)
#      inco_2 (opcion incorrecta 2)
#      inco_3 (opcion incorrecta 3)

def crearBaseDeDatos():
  conn = sqlite3.connect('base_de_datos.db')

  q = """
        CREATE TABLE IF NOT EXISTS jugadores 
        (
          nombre     TEXT UNIQUE NOT NULL PRIMARY KEY,
          puntos     INTEGER,
          tiempo     REAL
        );
      """

  conn.execute(q)

  q = """
        CREATE TABLE IF NOT EXISTS preguntas
        (
          id         INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
          tipo_ods   INTEGER NOT NULL,
          pregunta   TEXT UNIQUE NOT NULL,
          respuesta  TEXT UNIQUE NOT NULL,
          inco_1     TEXT UNIQUE NOT NULL,
          inco_2     TEXT UNIQUE NOT NULL,
          inco_3     TEXT UNIQUE NOT NULL
        );
      """

  conn.execute(q)
  
  conn.close()

def añadirPreguntas():
  conn = sqlite3.connect('base_de_datos.db')

  q = """
        INSERT OR IGNORE INTO preguntas (tipo_ods, pregunta, respuesta, inco_1, inco_2, inco_3)
        VALUES (1, '¿Cual es el índice de pobreza actual en ARGENTINA (estudio realizado en 2021)?', '37,3%', '40,7%', '55,2%', '12,2%')
        ;
      """

  conn.execute(q)
  conn.commit()

  q = """
        INSERT OR IGNORE INTO preguntas (tipo_ods, pregunta, respuesta, inco_1, inco_2, inco_3)
        VALUES (1, '¿Cuál es el porcentaje de la POBREZA en el mundo?', '85%', '77%', '35%', '42%')
        ;
      """

  conn.execute(q)
  conn.commit()

  q = """
        INSERT OR IGNORE INTO preguntas (tipo_ods, pregunta, respuesta, inco_1, inco_2, inco_3)
        VALUES (1, '¿Cual es el país MÁS pobre del mundo?', 'Burundi', 'Malaui', 'Venezuela', 'Haití')
        ;
      """

  conn.execute(q)
  conn.commit()

  q = """
        INSERT OR IGNORE INTO preguntas (tipo_ods, pregunta, respuesta, inco_1, inco_2, inco_3)
        VALUES (1, '¿En qué ZONAS se CENTRIFICA la pobreza mundial?', 'África', 'Asia Sur', 'Mediterraneo', 'Centroamérica')
        ;
      """

  conn.execute(q)
  conn.commit()

  q = """
        INSERT OR IGNORE INTO preguntas (tipo_ods, pregunta, respuesta, inco_1, inco_2, inco_3)
        VALUES (1, '¿Al mes, cuántas personas atraviesan la línea de pobreza en ARGENTINA?', '83 mil personas', '22 mil personas', '78 mil personas', '101 mil personas')
        ;
      """

  conn.execute(q)
  conn.commit()

  q = """
        INSERT OR IGNORE INTO preguntas (tipo_ods, pregunta, respuesta, inco_1, inco_2, inco_3)
        VALUES (2, '¿Aproximadamente, cuántos niños mueren al año por causas relacionadas con la desnutrición?', '2,8 millones', '6,9 millones', '4,5 millones', '1,3 millones')
        ;
      """

  conn.execute(q)
  conn.commit()

  q = """
        INSERT OR IGNORE INTO preguntas (tipo_ods, pregunta, respuesta, inco_1, inco_2, inco_3)
        VALUES (2, '¿Qué empresa NACIONAL contribuye al desarrollo de esta ODS?', 'Arcor', 'Sancor', 'Mercado Libre', 'Banco Macro')
        ;
      """

  conn.execute(q)
  conn.commit()

  q = """
        INSERT OR IGNORE INTO preguntas (tipo_ods, pregunta, respuesta, inco_1, inco_2, inco_3)
        VALUES (2, '¿Cual es el país con mayor desnutrición infantil según UNICEF en 2021?', 'República Democrática del Congo', 'Haití', 'India', 'Burkina Faso')
        ;
      """

  conn.execute(q)
  conn.commit()

  q = """
        INSERT OR IGNORE INTO preguntas (tipo_ods, pregunta, respuesta, inco_1, inco_2, inco_3)
        VALUES (2, '¿Cuál es el porcentaje de desnutrición en Argentina?', '40%', '30%', '50%', '65%')
        ;
      """

  conn.execute(q)
  conn.commit()

  q = """
        INSERT OR IGNORE INTO preguntas (tipo_ods, pregunta, respuesta, inco_1, inco_2, inco_3)
        VALUES (2, '¿Cuál es el organismo nacional que registra a los comedores y merenderos de todo el país?', 'Renacom', 'Ministerio de desarrollo social', 'Progresar', 'Comarg')
        ;
      """

  conn.execute(q)
  conn.commit()

  q = """
        INSERT OR IGNORE INTO preguntas (tipo_ods, pregunta, respuesta, inco_1, inco_2, inco_3)
        VALUES (3, '¿Qué porcentaje de la población Argentina no tiene ninguna cobertura de salud?', '36%', '50%', '67%', '23%')
        ;
      """

  conn.execute(q)
  conn.commit()

  q = """
        INSERT OR IGNORE INTO preguntas (tipo_ods, pregunta, respuesta, inco_1, inco_2, inco_3)
        VALUES (3, '¿Cuál es el índice de enfermeros por cada 10.000 personas en Argentina?', '4', '39', '51', '12')
        ;
      """

  conn.execute(q)
  conn.commit()

  q = """
        INSERT OR IGNORE INTO preguntas (tipo_ods, pregunta, respuesta, inco_1, inco_2, inco_3)
        VALUES (3, '¿Cuál es la esperanza de vida en Argentina?', '73,4 años', '65,7 años', '82 años', '90,3 años')
        ;
      """

  conn.execute(q)
  conn.commit()

  q = """
        INSERT OR IGNORE INTO preguntas (tipo_ods, pregunta, respuesta, inco_1, inco_2, inco_3)
        VALUES (3, '¿Cual es el porcentaje de muerte por enfermedades no transmisibles en Argentina?', '77%', '53,4%', '33,3%', '47%')
        ;
      """

  conn.execute(q)
  conn.commit()

  q = """
        INSERT OR IGNORE INTO preguntas (tipo_ods, pregunta, respuesta, inco_1, inco_2, inco_3)
        VALUES (3, '¿En qué región se vieron más causas de muerte por Covid-19?', 'América', 'Europa', 'África', 'Asia')
        ;
      """

  conn.execute(q)
  conn.commit()
  
  q = """
        INSERT OR IGNORE INTO preguntas (tipo_ods, pregunta, respuesta, inco_1, inco_2, inco_3)
        VALUES (4, '¿Cuánto dinero se piensa invertir en educación en Argentina este año?', '522 millones de pesos', '245 millones de pesos', '361 millones de pesos', '172 millones de pesos')
        ;
      """

  conn.execute(q)
  conn.commit()

  q = """
        INSERT OR IGNORE INTO preguntas (tipo_ods, pregunta, respuesta, inco_1, inco_2, inco_3)
        VALUES (4, '¿Cuántos niños, según UNICEF, no tienen acceso a la educación en Argentina?', '650 mil', '1,2 millones', '800 mil', '450 mil')
        ;
      """

  conn.execute(q)
  conn.commit()

  q = """
        INSERT OR IGNORE INTO preguntas (tipo_ods, pregunta, respuesta, inco_1, inco_2, inco_3)
        VALUES (4, '¿Cuál es el país con mayor porcentaje de niños sin escolarizar?', 'Sudán del Sur', 'Afganistán', 'Burundi', 'Surinam')
        ;
      """

  conn.execute(q)
  conn.commit()

  q = """
        INSERT OR IGNORE INTO preguntas (tipo_ods, pregunta, respuesta, inco_1, inco_2, inco_3)
        VALUES (4, '¿Cuál es uno de los objetivos de este ODS?', 'Garantizar una educación inclusiva y equitativa de calidad y promover oportunidades de aprendizaje a lo largo de la vida para todos', 'Promover la lectura y procurar que los alumnos tengan una mirada objetiva y crítica', 'Que los alumnos aprueben las materias', 'Crear materias en las cuales los alumnos puedan observar cuales son sus habilidades')
        ;
      """

  conn.execute(q)
  conn.commit()

  q = """
        INSERT OR IGNORE INTO preguntas (tipo_ods, pregunta, respuesta, inco_1, inco_2, inco_3)
        VALUES (4, '¿Qué empresa ayuda a que se cumpla este ODS?', 'Metrogas', 'Arcor', 'Motorola', 'Editorial Planeta')
        ;
      """

  conn.execute(q)
  conn.commit()

  conn.close()

def devolverPregunta():
  conn = sqlite3.connect('base_de_datos.db')
  lista = []
  orden = []
  ordenODS1 = []
  ordenODS2 = []
  ordenODS3 = []
  ordenODS4 = []
  
  q = f"""
        SELECT id, pregunta, respuesta, inco_1, inco_2, inco_3
        FROM preguntas
        ;
      """

  resu = conn.execute(q)
  for fila in resu:
    lista.append(fila)

  i = 0
  while i < 5:
    preg = lista[randint(0, 4)]
    if preg not in ordenODS1:
      ordenODS1.append(preg)
      i += 1

  i = 0
  while i < 5:
    preg = lista[randint(5, 9)]
    if preg not in ordenODS2:
      ordenODS2.append(preg)
      i += 1

  i = 0
  while i < 5:
    preg = lista[randint(10, 14)]
    if preg not in ordenODS3:
      ordenODS3.append(preg)
      i += 1

  i = 0
  while i < 5:
    preg = lista[randint(15, 19)]
    if preg not in ordenODS4:
      ordenODS4.append(preg)
      i += 1

  orden = [ordenODS1, ordenODS2, ordenODS3, ordenODS4]
  
  return orden

def crearPuestosLibres():
  conn = sqlite3.connect('base_de_datos.db')

  q = """
        INSERT OR IGNORE INTO jugadores (nombre, puntos, tiempo)
        VALUES ('null01', 0, 999999999.0)
      """

  conn.execute(q)
  conn.commit()

  q = """
        INSERT OR IGNORE INTO jugadores (nombre, puntos, tiempo)
        VALUES ('null02', 0, 999999999.0)
      """

  conn.execute(q)
  conn.commit()

  q = """
        INSERT OR IGNORE INTO jugadores (nombre, puntos, tiempo)
        VALUES ('null03', 0, 999999999.0)
      """

  conn.execute(q)
  conn.commit()

  q = """
        INSERT OR IGNORE INTO jugadores (nombre, puntos, tiempo)
        VALUES ('null04', 0, 999999999.0)
      """

  conn.execute(q)
  conn.commit()
  
def devolverMejores():
  conn = sqlite3.connect('base_de_datos.db')
  lista = []
  
  q = """
        SELECT *
        FROM jugadores
        ORDER BY puntos DESC, tiempo
        LIMIT 5
        ;
      """
  
  resu = conn.execute(q)

  for fila in resu:
    lista.append(fila)

  return lista
    
def añadirJugador(jug):
  conn = sqlite3.connect('base_de_datos.db')

  q = f"""
        INSERT INTO jugadores (nombre, puntos, tiempo)
        VALUES ('{jug}', 0, 0.0)
        ;
      """

  conn.execute(q)
  conn.commit()

  conn.close()

def registrarDatos(jug, pun, tie):
  conn = sqlite3.connect('base_de_datos.db')

  q = f"""
        UPDATE jugadores 
        SET puntos = {pun}, tiempo = '{tie}'
        WHERE nombre = '{jug}'
        ;
      """

  conn.execute(q)
  conn.commit()

  conn.close()
  
def listaJugadores():
  conn = sqlite3.connect('base_de_datos.db')
  lista = []
  
  q = f"""
        SELECT nombre
        FROM jugadores
        ;
      """

  resu = conn.execute(q)

  for fila in resu:
    lista.append(fila[0])
  conn.close()
  
  return lista

def girarRuleta():
  global contadorPreguntaODS1
  global contadorPreguntaODS2
  global contadorPreguntaODS3
  global contadorPreguntaODS4
  global preguntasUsadas
  num = randint(1, 4)
  if num == 1 and contadorPreguntaODS1 < 4:
    ods = "Fin de la pobreza"
  elif num == 2 and contadorPreguntaODS2 < 4:
    ods = "Hambre cero"
  elif num == 3 and contadorPreguntaODS3 < 4:
    ods = "Salud y bienestar"
  elif num == 4 and contadorPreguntaODS4 < 4:
    ods = "Educación de calidad"
  else:
    return girarRuleta()
  return [num, f"El ODS seleccionado es: ODS {num}: '{ods}'"]

ods = 1
puntos = 0
tiempoComienzo = 0
tiempoFin = 0
tiempo = 0
pregunta = 0
contadorPreguntaODS1 = -1
contadorPreguntaODS2 = -1
contadorPreguntaODS3 = -1
contadorPreguntaODS4 = -1

@app.route('/')
def index():
  crearBaseDeDatos()
  añadirPreguntas()
  crearPuestosLibres()
  global tiempoComienzo
  global tiempoFin
  global tiempo
  global pregunta
  global ods
  global puntos
  global contadorPreguntaODS1
  global contadorPreguntaODS2
  global contadorPreguntaODS3
  global contadorPreguntaODS4
  pregunta = devolverPregunta()
  ods = 1
  puntos = 0
  tiempoComienzo = 0
  tiempoFin = 0
  tiempo = 0
  contadorPreguntaODS1 = -1
  contadorPreguntaODS2 = -1
  contadorPreguntaODS3 = -1
  contadorPreguntaODS4 = -1
  return render_template('index.html')

@app.route('/ingresa_nombre')
def ingresarDatos():
  global puntos
  puntos = 0
  return render_template('usuario.html', jugadores = listaJugadores())

@app.route('/ruleta', methods=['GET', 'POST'])
def ruleta():
  global puntos
  global ods
  nombreJugador = request.form['nombreJugador']
  if puntos == 0:
    añadirJugador(nombreJugador)
  ods = girarRuleta()
  return render_template('ruleta.html', res = ods, jug = nombreJugador)

@app.route('/pregunta', methods=['GET', 'POST'])
def pregunta():
  global ods
  global tiempoComienzo
  global tiempo
  global puntos
  global pregunta
  global contadorPreguntaODS1
  global contadorPreguntaODS2
  global contadorPreguntaODS3
  global contadorPreguntaODS4
  tiempoComienzo = time.time()
  nombreJugador = request.form['nombreJugador']
  
  if ods[0] == 1:
    contadorPreguntaODS1 += 1
    return render_template('pregunta.html', pre = pregunta[ods[0]-1][contadorPreguntaODS1], jug = nombreJugador, pun = puntos, sum = contadorPreguntaODS1 + contadorPreguntaODS2 + contadorPreguntaODS3 + contadorPreguntaODS4)
  elif ods[0] == 2:
    contadorPreguntaODS2 += 1
    return render_template('pregunta.html', pre = pregunta[ods[0]-1][contadorPreguntaODS2], jug = nombreJugador, pun = puntos, sum = contadorPreguntaODS1 + contadorPreguntaODS2 + contadorPreguntaODS3 + contadorPreguntaODS4)
  elif ods[0] == 3:
    contadorPreguntaODS3 += 1
    return render_template('pregunta.html', pre = pregunta[ods[0]-1][contadorPreguntaODS3], jug = nombreJugador, pun = puntos, sum = contadorPreguntaODS1 + contadorPreguntaODS2 + contadorPreguntaODS3 + contadorPreguntaODS4)
  elif ods[0] == 4:
    contadorPreguntaODS4 += 1
    return render_template('pregunta.html', pre = pregunta[ods[0]-1][contadorPreguntaODS4], jug = nombreJugador, pun = puntos, sum = contadorPreguntaODS1 + contadorPreguntaODS2 + contadorPreguntaODS3 + contadorPreguntaODS4)

@app.route('/perdiste', methods=['GET', 'POST'])
def perder():
  global tiempoComienzo
  global tiempoFin
  global tiempo
  tiempoFin = time.time()
  tiempo += tiempoFin - tiempoComienzo
  nombreJugador = request.form['nombreJugador']
  registrarDatos(nombreJugador, puntos, round(tiempo, 2))
  return render_template('perdiste.html')

@app.route('/correcto', methods=['GET', 'POST'])
def correcto():
  global puntos
  global tiempoComienzo
  global tiempoFin
  global tiempo
  global contadorPreguntaODS1
  global contadorPreguntaODS2
  global contadorPreguntaODS3
  global contadorPreguntaODS4
  tiempoFin = time.time()
  tiempo += tiempoFin - tiempoComienzo
  puntos += 1
  nombreJugador = request.form['nombreJugador']
  return render_template('correcto.html', jug = nombreJugador, contador = contadorPreguntaODS1 + contadorPreguntaODS2 + contadorPreguntaODS3 + contadorPreguntaODS4)

@app.route('/ganaste', methods=['GET', 'POST'])
def ganar():
  global tiempo
  global puntos
  nombreJugador = request.form['nombreJugador']
  registrarDatos(nombreJugador, puntos, round(tiempo, 2))
  return render_template('ganaste.html')

@app.route('/puntajes')
def tablaPuntajes():
  return render_template('leaderboard.html', mejoresJugadores = devolverMejores())

app.run(host='0.0.0.0', port=81)
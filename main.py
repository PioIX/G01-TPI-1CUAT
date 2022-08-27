from flask import Flask, render_template, request
from random import randint
import sqlite3
import time

app = Flask(__name__)

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
        VALUES (1, '¿CUAL ES EL ÍNDICE DE POBREZA ACTUAL EN ARGENTINA (ESTUDIO REALIZADO EN 2021)?', '37,3%', '40,7%', '55,2%', '12,2%')
        ;
      """

  conn.execute(q)
  conn.commit()

  q = """
        INSERT OR IGNORE INTO preguntas (tipo_ods, pregunta, respuesta, inco_1, inco_2, inco_3)
        VALUES (1, '¿CUÁL ES EL PORCENTAJE DE LA POBREZA EN EL MUNDO?', '85%', '77%', '35%', '42%')
        ;
      """

  conn.execute(q)
  conn.commit()

  q = """
        INSERT OR IGNORE INTO preguntas (tipo_ods, pregunta, respuesta, inco_1, inco_2, inco_3)
        VALUES (1, '¿CUÁL ES EL PAÍS MÁS POBRE DEL MUNDO?', 'Burundi', 'Malaui', 'Venezuela', 'Haití')
        ;
      """

  conn.execute(q)
  conn.commit()

  q = """
        INSERT OR IGNORE INTO preguntas (tipo_ods, pregunta, respuesta, inco_1, inco_2, inco_3)
        VALUES (1, '¿EN QUÉ ZONAS SE CENTRIFICA LA POBREZA MUNDIAL?', 'África', 'Asia Sur', 'Mediterraneo', 'Centroamérica')
        ;
      """

  conn.execute(q)
  conn.commit()

  q = """
        INSERT OR IGNORE INTO preguntas (tipo_ods, pregunta, respuesta, inco_1, inco_2, inco_3)
        VALUES (1, '¿AL MES, CUÁNTAS PERSONAS ATRAVIESAN LA LÍNEA DE POBREZA EN ARGENTINA?', '83 mil personas', '22 mil personas', '78 mil personas', '101 mil personas')
        ;
      """

  conn.execute(q)
  conn.commit()

  q = """
        INSERT OR IGNORE INTO preguntas (tipo_ods, pregunta, respuesta, inco_1, inco_2, inco_3)
        VALUES (2, '¿APROXIMADAMENTE, CUÁNTOS NIÑOS MUEREN AL AÑO POR CAUSAS RELACIONADAS CON LA DESNUTRICIÓN?', '2,8 millones', '6,9 millones', '4,5 millones', '1,3 millones')
        ;
      """

  conn.execute(q)
  conn.commit()

  q = """
        INSERT OR IGNORE INTO preguntas (tipo_ods, pregunta, respuesta, inco_1, inco_2, inco_3)
        VALUES (2, '¿QUÉ EMPRESA NACIONAL CONTRIBUYE AL DESARROLLO DE ESTA ODS?', 'Arcor', 'Sancor', 'Mercado Libre', 'Banco Macro')
        ;
      """

  conn.execute(q)
  conn.commit()

  q = """
        INSERT OR IGNORE INTO preguntas (tipo_ods, pregunta, respuesta, inco_1, inco_2, inco_3)
        VALUES (2, '¿CUÁL ES EL PAÍS CON MAYOR DESNUTRICIÓN INFANTIL SEGÚN UNICEF EN 2021?', 'República Democrática del Congo', 'Haití', 'India', 'Burkina Faso')
        ;
      """

  conn.execute(q)
  conn.commit()

  q = """
        INSERT OR IGNORE INTO preguntas (tipo_ods, pregunta, respuesta, inco_1, inco_2, inco_3)
        VALUES (2, '¿CUÁL ES EL PORCENTAJE DE DESNUTRICIÓN EN ARGENTINA?', '40%', '30%', '50%', '65%')
        ;
      """

  conn.execute(q)
  conn.commit()

  q = """
        INSERT OR IGNORE INTO preguntas (tipo_ods, pregunta, respuesta, inco_1, inco_2, inco_3)
        VALUES (2, '¿CUÁL ES EL ORGANISMO NACIONAL QUE REGISTRA A LOS COMEDORES Y MERENDEROS DE TODO EL PAÍS?', 'Renacom', 'Ministerio de desarrollo social', 'Progresar', 'Comarg')
        ;
      """

  conn.execute(q)
  conn.commit()

  q = """
        INSERT OR IGNORE INTO preguntas (tipo_ods, pregunta, respuesta, inco_1, inco_2, inco_3)
        VALUES (3, '¿QUÉ PORCENTAJE DE LA POBLACIÓN ARGENTINA NO TIENE NINGUNA COBERTURA DE SALUD?', '36%', '50%', '67%', '23%')
        ;
      """

  conn.execute(q)
  conn.commit()

  q = """
        INSERT OR IGNORE INTO preguntas (tipo_ods, pregunta, respuesta, inco_1, inco_2, inco_3)
        VALUES (3, '¿CUÁL ES EL ÍNDICE DE ENFERMEROS POR CADA 10.000 PERSONAS EN ARGENTINA?', '4', '39', '51', '12')
        ;
      """

  conn.execute(q)
  conn.commit()

  q = """
        INSERT OR IGNORE INTO preguntas (tipo_ods, pregunta, respuesta, inco_1, inco_2, inco_3)
        VALUES (3, '¿CUÁL ES LA ESPERANZA DE VIDA EN ARGENTINA?', '73,4 años', '65,7 años', '82 años', '90,3 años')
        ;
      """

  conn.execute(q)
  conn.commit()

  q = """
        INSERT OR IGNORE INTO preguntas (tipo_ods, pregunta, respuesta, inco_1, inco_2, inco_3)
        VALUES (3, '¿CUÁL ES EL PORCENTAJE DE MUERTE POR ENFERMEDADES NO TRANSMISIBLES EN ARGENTINA?', '77%', '53,4%', '33,3%', '47%')
        ;
      """

  conn.execute(q)
  conn.commit()

  q = """
        INSERT OR IGNORE INTO preguntas (tipo_ods, pregunta, respuesta, inco_1, inco_2, inco_3)
        VALUES (3, '¿EN QUÉ REGIÓN SE VIERON MÁS CAUSAS DE MUERTE POR COVID-19?', 'América', 'Europa', 'África', 'Asia')
        ;
      """

  conn.execute(q)
  conn.commit()
  
  q = """
        INSERT OR IGNORE INTO preguntas (tipo_ods, pregunta, respuesta, inco_1, inco_2, inco_3)
        VALUES (4, '¿CUÁNTO DINERO SE PIENSA INVERTIR EN EDUCACIÓN EN ARGENTINA ESTE AÑO?', '522 millones de pesos', '245 millones de pesos', '361 millones de pesos', '172 millones de pesos')
        ;
      """

  conn.execute(q)
  conn.commit()

  q = """
        INSERT OR IGNORE INTO preguntas (tipo_ods, pregunta, respuesta, inco_1, inco_2, inco_3)
        VALUES (4, '¿CUÁNTOS NIÑOS, SEGÚN UNICEF, NO TIENEN ACCESO A LA EDUCACIÓN EN ARGENTINA?', '650 mil', '1,2 millones', '800 mil', '450 mil')
        ;
      """

  conn.execute(q)
  conn.commit()

  q = """
        INSERT OR IGNORE INTO preguntas (tipo_ods, pregunta, respuesta, inco_1, inco_2, inco_3)
        VALUES (4, '¿CUÁL ES EL PAÍS CON MAYOR PORCENTAJE DE NIÑOS SIN ESCOLARIZAR?', 'Sudán del Sur', 'Afganistán', 'Burundi', 'Surinam')
        ;
      """

  conn.execute(q)
  conn.commit()

  q = """
        INSERT OR IGNORE INTO preguntas (tipo_ods, pregunta, respuesta, inco_1, inco_2, inco_3)
        VALUES (4, '¿CUÁL ES UNO DE LOS OBJETIVOS DE ESTE ODS?', 'Garantizar una educación inclusiva y equitativa de calidad y promover oportunidades de aprendizaje a lo largo de la vida para todos', 'Promover la lectura y procurar que los alumnos tengan una mirada objetiva y crítica', 'Que los alumnos aprueben las materias', 'Crear materias en las cuales los alumnos puedan observar cuales son sus habilidades')
        ;
      """

  conn.execute(q)
  conn.commit()

  q = """
        INSERT OR IGNORE INTO preguntas (tipo_ods, pregunta, respuesta, inco_1, inco_2, inco_3)
        VALUES (4, '¿QUÉ EMPRESA AYUDA A QUE SE CUMPLA ESTE ODS?', 'Metrogas', 'Arcor', 'Motorola', 'Editorial Planeta')
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
    global puntos
    global tiempoComienzo
    global tiempoFin
    global tiempo
    global pregunta
    global contadorPreguntaODS1
    global contadorPreguntaODS2
    global contadorPreguntaODS3
    global contadorPreguntaODS4
    puntos = 0
    tiempoComienzo = 0
    tiempoFin = 0
    tiempo = 0
    pregunta = devolverPregunta()
    contadorPreguntaODS1 = -1
    contadorPreguntaODS2 = -1
    contadorPreguntaODS3 = -1
    contadorPreguntaODS4 = -1
    return render_template('index.html')
  
@app.route('/usuario')
def ingresarDatos():
    global puntos
    puntos = 0
    return render_template('usuario.html', jugadores = listaJugadores())

@app.route('/ruleta', methods=['GET', 'POST'])
def ruleta():
    global puntos
    global contadorPreguntaODS1
    global contadorPreguntaODS2
    global contadorPreguntaODS3
    global contadorPreguntaODS4
    nombreJugador = request.form['nombreJugador']
    if puntos == 0:
      añadirJugador(nombreJugador)

    tipoRuleta = ""
    if contadorPreguntaODS1 < 4:
      tipoRuleta += "one"
    if contadorPreguntaODS2 < 4:
      tipoRuleta += "two"
    if contadorPreguntaODS3 < 4:
      tipoRuleta += "three"
    if contadorPreguntaODS4 < 4:
      tipoRuleta += "four"
    if tipoRuleta == "onetwothreefour":
      tipoRuleta = "complete"
    tipoRuleta += "wheel.png"

    if tipoRuleta == 'completewheel.png':
      grados = 90
    elif tipoRuleta == 'onetwothreewheel.png' or tipoRuleta == 'onethreefourwheel.png' or tipoRuleta == 'onetwofourwheel.png' or tipoRuleta == 'twothreefourwheel.png':
      grados = 120
    elif tipoRuleta == 'onetwowheel.png' or tipoRuleta == 'onethreewheel.png' or tipoRuleta == 'onefourwheel.png' or tipoRuleta == 'twothreewheel.png' or tipoRuleta == 'twofourwheel.png' or tipoRuleta == 'threefourwheel.png':
      grados = 180
    else:
      grados = 360

    listaPreguntas = ""
  
    if tipoRuleta == 'completewheel.png':
      listaPreguntas = "{1: [1, `ODS 1: 'Fin de la pobreza'`], 2: [3, `ODS 3: 'Salud y bienestar'`], 3: [4, `ODS 4: 'Educación de calidad'`], 4: [2, `ODS 2: 'Hambre cero'`]}"
    elif tipoRuleta == 'onewheel.png':
      listaPreguntas = "{1: [1, `ODS 1: 'Fin de la pobreza'`]}"
    elif tipoRuleta == 'twowheel.png':
      listaPreguntas = "{1: [2, `ODS 2: 'Hambre cero'`]}"
    elif tipoRuleta == 'threewheel.png':
      listaPreguntas = "{1: [3, `ODS 3: 'Salud y bienestar'`]}"
    elif tipoRuleta == 'fourwheel.png':
      listaPreguntas = "{1: [4, `ODS 4: 'Educación de calidad'`]}"
    elif tipoRuleta == 'onetwowheel.png':
      listaPreguntas = "{1: [1, `ODS 1: 'Fin de la pobreza'`], 2: [2, `ODS 2: 'Hambre cero'`]}"
    elif tipoRuleta == 'onethreewheel.png':
      listaPreguntas = "{1: [1, `ODS 1: 'Fin de la pobreza'`], 2: [3, `ODS 3: 'Salud y bienestar'`]}"
    elif tipoRuleta == 'onefourwheel.png':
      listaPreguntas = "{1: [1, `ODS 1: 'Fin de la pobreza'`], 2: [4, `ODS 4: 'Educación de calidad'`]}"
    elif tipoRuleta == 'twothreewheel.png':
      listaPreguntas = "{1: [2, `ODS 2: 'Hambre cero'`], 2: [3, `ODS 3: 'Salud y bienestar'`]}"
    elif tipoRuleta == 'twofourwheel.png':
      listaPreguntas = "{1: [2, `ODS 2: 'Hambre cero'`], 2: [4, `ODS 4: 'Educación de calidad'`]}"
    elif tipoRuleta == 'threefourwheel.png':
      listaPreguntas = "{1: [3, `ODS 3: 'Salud y bienestar'`], 2: [4, `ODS 4: 'Educación de calidad'`]}"
    elif tipoRuleta == 'onetwothreewheel.png':
      listaPreguntas = "{1: [1, `ODS 1: 'Fin de la pobreza'`], 2: [3, `ODS 3: 'Salud y bienestar'`], 3: [2, `ODS 2: 'Hambre cero'`]}"
    elif tipoRuleta == 'onetwofourwheel.png':
      listaPreguntas = "{1: [1, `ODS 1: 'Fin de la pobreza'`], 2: [4, `ODS 4: 'Educación de calidad'`], 3: [2, `ODS 2: 'Hambre cero'`]}"
    elif tipoRuleta == 'onethreefourwheel.png':
      listaPreguntas = "{1: [1, `ODS 1: 'Fin de la pobreza'`], 2: [4, `ODS 4: 'Educación de calidad'`], 3: [3, `ODS 3: 'Salud y bienestar'`]}"  
    elif tipoRuleta == 'twothreefourwheel.png.png':
      listaPreguntas = "{1: [2, `ODS 2: 'Hambre cero'`], 2: [4, `ODS 4: 'Educación de calidad'`], 3: [3, `ODS 3: 'Salud y bienestar'`]}"
  
    return render_template('ruleta.html', jug = nombreJugador, pregs = listaPreguntas, rul = tipoRuleta, deg = grados)

@app.route('/pregunta', methods=['GET', 'POST'])
def pregunta():
    global puntos
    global pregunta
    global tiempoComienzo
    global contadorPreguntaODS1
    global contadorPreguntaODS2
    global contadorPreguntaODS3
    global contadorPreguntaODS4
    nombreJugador = request.form['nombreJugador']
    odsSeleccionado = request.form['odsSeleccionado']
    tiempoComienzo = time.time()
    if int(odsSeleccionado) == 1:
      contadorPreguntaODS1 += 1
      return render_template('pregunta.html', jug = nombreJugador, pre = pregunta[int(odsSeleccionado)-1][contadorPreguntaODS1], pun = puntos, tipo = 'fondo-ods1')
    elif int(odsSeleccionado) == 2:
      contadorPreguntaODS2 += 1
      return render_template('pregunta.html', jug = nombreJugador, pre = pregunta[int(odsSeleccionado)-1][contadorPreguntaODS2], pun = puntos, tipo = 'fondo-ods2')
    elif int(odsSeleccionado) == 3:
      contadorPreguntaODS3 += 1
      return render_template('pregunta.html', jug = nombreJugador, pre = pregunta[int(odsSeleccionado)-1][contadorPreguntaODS3], pun = puntos, tipo = 'fondo-ods3')
    elif int(odsSeleccionado) == 4:
      contadorPreguntaODS4 += 1
      return render_template('pregunta.html', jug = nombreJugador, pre = pregunta[int(odsSeleccionado)-1][contadorPreguntaODS4], pun = puntos, tipo = 'fondo-ods4')

@app.route('/perdiste', methods=['GET', 'POST'])
def perder():
  global tiempoComienzo
  global tiempoFin
  global tiempo
  tiempoFin = time.time()
  tiempo += tiempoFin - tiempoComienzo
  nombreJugador = request.form['nombreJugador']
  registrarDatos(nombreJugador, puntos, round(tiempo, 2))
  return render_template('perdiste.html', jug = nombreJugador)

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
  return render_template('ganaste.html', jug = nombreJugador)

@app.route('/puntajes', methods=['GET', 'POST'])
def tablaPuntajes():
  nombreJugador = request.form['nombreJugador']
  return render_template('leaderboard.html', mejoresJugadores = devolverMejores(), jug = nombreJugador)

app.run(host='0.0.0.0', port=81)
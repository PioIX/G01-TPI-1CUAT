# Trabajo integrador interdisciplinario Grupo N°01

## Integrantes:

* Lucas Bertoli
* Bautista Della Penna
* Manuel Ledo
* Bono Neer
* Matías Torre

## Introducción:

Vamos a desarrollar una aplicación web que permita mostrar los conocimientos del usuario acerca de los ODS “Fin de la Pobreza” (ODS 1), “Hambre Cero” (ODS 2), “Salud y Bienestar” (ODS 3) y “Educación de Calidad” (ODS 4). Al iniciar el juego, se pide al usuario que ingrese un nombre que sirve como id, por ello agregaríamos una validación de datos para que no se pueda repetir, en la base de datos donde se registrarán sus puntos (y quizás el tiempo de juego). A continuación, empezaría el juego principal, que tendrá formato de Trivia, en el que se seleccionará uno de los cuatro temas mediante una ruleta. Luego se hará una pregunta del ODS y se darán 4 opciones, de las cuales solo una es correcta. Responder bien sumará un punto, y responder mal haría que termine la partida. Al perder, se mostraría una pantalla de “¡Perdiste!”, y luego la pantalla de puntuaciones; si se respondieron todas las preguntas, se mostraría directamente la pantalla de puntuaciones. En esta hay una tabla en la que se muestran los 5 mejores jugadores. Para ordenarlos se priorizarían los puntos, pero en caso de empate, el jugador que respondió en menos tiempo aparecerá más arriba.

## App de Flask:
https://replit.com/@Bono-EzequielEz/Proyecto-Interdisciplinario-CUAT-1#main.py

## App en PythonAnywhere:
http://neerbono.pythonanywhere.com/

## Presupuesto:
https://docs.google.com/document/d/1xGO1DjLv1bD5pJyI-0qKa4lQ6samu9PrN9SNyLDruPM/edit?usp=sharing

## Preguntas y Respuestas - Reglas y Puntajes:
https://docs.google.com/document/d/17-RT-5bg9aNww0IV8ExO2MLYFmJeNQCS9yjR2734ilE/edit

## Índice:
### Templates:
* Contiene los archivos '.html' que se usan en la app.
### Static:
* Contiene el archivo 'styles.css' que se usa en la app.
  ### img:
* Contiene las imágenes que se usan en la app.
    ### fondos:
* Contiene las imágenes utilizadas como fondos.
    ### ruletas:
* Contiene las imágenes de todas las ruletas utilizadas.
### Sin carpeta:
* el archivo de 'main.py'
* la base de datos

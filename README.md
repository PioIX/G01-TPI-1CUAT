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
https://replit.com/@Bono-EzequielEz/G01-Proyecto-Interdisciplinario-1-1

## Presupuesto:
https://docs.google.com/document/d/1xGO1DjLv1bD5pJyI-0qKa4lQ6samu9PrN9SNyLDruPM/edit?usp=sharing

## Índice:
### Templates:
* Contiene los archivos '.html' que se usan en la app.
### CSS:
* Contiene el archivo '.css' que se usa en la app.
### img:
* Contiene las imagenes que se usan en la app.
### Docs:
* Contiene el documento con las preguntas, sus respuestas y las reglas del juego.
### Base de datos:
* Contiene la base de datos

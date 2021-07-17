import turtle
import time

import random

posponer = 0.1

score = 0
highScore = 0

window = turtle.Screen()
window.title("Juego Snake")
window.bgcolor("black")
window.setup(width = 600, height = 600)
window.tracer(0)

cabeza = turtle.Turtle()
cabeza.speed(0)
cabeza.shape("square")
cabeza.penup()
cabeza.goto(0,0)
cabeza.direction = "stop"
cabeza.color("blue")

comida = turtle.Turtle()
comida.speed(0)
comida.shape("circle")
comida.penup()
comida.goto(0,100)
comida.color("red")

segmentos = []

texto = turtle.Turtle()
texto.speed(0)
texto.color("white")
texto.penup()
texto.hideturtle()
texto.goto(0, 260)
texto.write("Score: 0       High Score: 0", align = "center", font = ("Courier", 20, "normal"))

def arriba():
	cabeza.direction = "up"

def abajo():
	cabeza.direction = "down"

def izquierda():
	cabeza.direction = "left"

def derecha():
	cabeza.direction = "right"


def mov():
	if cabeza.direction == "up":
		y = cabeza.ycor()
		cabeza.sety(y + 20)

	if cabeza.direction == "down":
		y = cabeza.ycor()
		cabeza.sety(y - 20)

	if cabeza.direction == "left":
		x = cabeza.xcor()
		cabeza.setx(x - 20)

	if cabeza.direction == "right":
		x = cabeza.xcor()
		cabeza.setx(x + 20)

window.listen()
window.onkeypress(arriba, "Up")
window.onkeypress(abajo, "Down")
window.onkeypress(izquierda, "Left")
window.onkeypress(derecha, "Right")

while True:
	window.update()

	if cabeza.xcor()> 280 or cabeza.xcor() < -280 or cabeza.ycor() > 280 or cabeza.ycor() < -280:
		time.sleep(1)
		cabeza.goto(0,0)
		cabeza.direction = "stop"
		for segmento in segmentos:
			segmento.goto(2000, 2000)

		segmentos = []
		score = 0
		texto.clear()
		texto.write("Score: {}       High Score: {}".format(score, highScore), align = "center", font = ("Courier", 20, "normal"))



	if cabeza.distance(comida) < 20:
		x = random.randint(-280, 280)
		y = random.randint(-280, 280)
		comida.goto(x,y)

		nuevoSegmento = turtle.Turtle()
		nuevoSegmento.speed(0)
		nuevoSegmento.shape("square")
		nuevoSegmento.penup()
		nuevoSegmento.color("blue")
		segmentos.append(nuevoSegmento)

		score += 10

		if score > highScore:
			highScore = score

		texto.clear()
		texto.write("Score: {}       High Score: {}".format(score, highScore), align = "center", font = ("Courier", 20, "normal"))


	totalSeg = len(segmentos)
	for index in range(totalSeg - 1, 0, -1):
		x = segmentos[index - 1].xcor()
		y = segmentos[index - 1].ycor()
		segmentos[index].goto(x, y)

	if totalSeg > 0:
		x = cabeza.xcor()
		y = cabeza.ycor()
		segmentos[0].goto(x,y)

	mov()

	for segmento in segmentos:
		if segmento.distance(cabeza) < 20:
			time.sleep(1)
			cabeza.goto(0,0)
			cabeza.direction = "stop"

			for segmento in segmentos:
				segmento.goto(2000, 2000)
			segmentos = []

			score = 0
			texto.clear()
			texto.write("Score: {}       High Score: {}".format(score, highScore), align = "center", font = ("Courier", 20, "normal"))


	time.sleep(posponer)

turtle.exitonclick()
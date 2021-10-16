from turtle import Turtle
from turtle import Screen
import random

carrera = False
pantalla = Screen()
pantalla.setup(width=500, height=400)
pantalla.bgcolor("#94FF33")
tortuga_elegida = pantalla.textinput(title="Haz tu apuesta!", prompt="Con qué tortuga quieres concursar? Elige un color: ")
tortugas = []
colores = ["red", "orange", "yellow", "green", "blue", "purple"]

for tortuga_index in range(6):
	nueva_tortuga = Turtle(shape="turtle")
	nueva_tortuga.color(colores[tortuga_index])
	nueva_tortuga.penup()
	nueva_tortuga.goto(x=-230, y=-75 + tortuga_index * 30)

	tortugas.append(nueva_tortuga)

if tortuga_elegida:
	carrera = True

while carrera:
	for tortuga in tortugas:
		distancia = random.randint(0, 10)
		tortuga.forward(distancia)
		
		# cuando llega a la meta
		if tortuga.xcor()>230:
			carrera = False
			ganadora = tortuga.pencolor()
			
			if ganadora == tortuga_elegida:
				print("GANASTE!!! La tortuga "+ganadora+" es la vencedora")
			else:
				print("PERDISTE!!! La tortuga "+ganadora+" es la vencedora")


# nos va a ayudar a cerrar la pantalla
pantalla.exitonclick()

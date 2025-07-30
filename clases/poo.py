import turtle

class Tortuga():
    def __init__(self, color, size, speed):
        self.tortuga = turtle.Turtle()
        self.tortuga.color(color)
        self.tortuga.pensize(size)
        self.tortuga.speed(speed)


    def mover_arriba(self):
        y = self.tortuga.ycor()
        self.tortuga.sety(y + 20)

    def mover_abajo(self):
        y = self.tortuga.ycor()
        self.tortuga.sety(y - 20)

    def mover_izquierda(self):
        x = self.tortuga.xcor()
        self.tortuga.setx(x - 20)

    def mover_derecha(self):
        x = self.tortuga.xcor()
        self.tortuga.setx(x + 20)

ventana = turtle.Screen()
ventana.title("Tortuga")
ventana.bgcolor("black")

tortuga = Tortuga("green", 5, 5)
ventana.listen()
ventana.onkey(tortuga.mover_arriba, "w")
ventana.onkey(tortuga.mover_abajo, "s")
ventana.onkey(tortuga.mover_izquierda, "a")
ventana.onkey(tortuga.mover_derecha, "d")

turtle.done()
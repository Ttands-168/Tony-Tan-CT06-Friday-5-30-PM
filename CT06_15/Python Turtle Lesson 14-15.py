import turtle
import math
Fiona = turtle.Turtle()
Fiona.seth(0)
Fiona.shape("turtle")
Fiona.speed(10)
Fiona.pendown()
for x in range(1, 3):
    Fiona.forward(85)
    Fiona.right(90)
    Fiona.forward(20)
    Fiona.left(90)
    Fiona.forward(5)

del Fiona
Celeste = math.degrees(90)
print(Celeste)

del Celeste # but Celeste only becomes a comment now


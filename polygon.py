import turtle

turtle.Screen().bgcolor("orange")
turtle.Screen().setup(300,400)

pen = turtle.Turtle()

numbersides = 6 
sidelength = 70

angle = 360.0 / numbersides

for i in range(6) :
     pen.forward(sidelength)
     pen.right(angle)
turtle.done()
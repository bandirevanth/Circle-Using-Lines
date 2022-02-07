import turtle

turtle.speed(100)
turtle.color('blue','green')
turtle.begin_fill()

while True:
    turtle.forward(200)
    turtle.left(170)
    if abs(turtle.pos())<1:
        break

turtle.done()

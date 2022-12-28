
import turtle

turtle.bgcolor("darkred")
turtle.speed(100)

turtle.penup()
turtle.goto(-55,-90) 
turtle.pendown()

turtle.pensize(2)
turtle.pencolor("yellow")
turtle.circle(140) 

turtle.penup()
turtle.fd(200)
turtle.lt(85)
turtle.fd(400)
turtle.rt(45)
turtle.pendown()

turtle.fillcolor("#fdc04e")
turtle.begin_fill()

turtle.pensize(2)
turtle.backward(350)
turtle.rt(45)
turtle.fd(80)
turtle.rt(-45)

turtle.backward(200)
turtle.rt(45)
turtle.fd(80)
turtle.rt(-45)

turtle.backward(350)
turtle.rt(5)
turtle.fd(450)
turtle.rt(37)

turtle.backward(80)
turtle.lt(45)
turtle.fd(170)
turtle.rt(45)

turtle.backward(60)
turtle.lt(54)
turtle.fd(155)

turtle.end_fill()
turtle.mainloop()






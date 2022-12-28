import turtle

turtle.hideturtle()
turtle.bgcolor("red")
turtle.setup(1000, 700)
turtle.title("Mulher Maravilha")

turtle.speed(2)

part1Gold = [(0,0), (-30,40), (0, 80), (30,40), (0,0)]


part2Gold = [(0, 90), (-34, 45), (-64, 85), (-20, 140), (-35, 150), (-20, 160), (10, 160), (64, 85), (34, 45), (0,90)]


part3Gold = [(-4, -4), (-128, 160), (-400, 160), (-370, 120), (-153, 120), (-31, -41), (-4, -4)]


part4Gold = [(4, -4), (128, 160), (400, 160),  (370, 120), (153, 120), (31, -41), (4, -4)]


part5Gold = [(-366, 115), (-156, 115), (-69, 0), (-96, -37), (-181, 75), (-336, 75), (-366, 115)]


part6Gold = [(366, 115), (156, 115), (69, 0), (96, -37), (181, 75), (336, 75), (366, 115)]


part7Gold = [(-35, -45),(-66, -4), (-96, -45),(-184, 70),(-332, 70),(-302, 30),(-206, 30),(-94, -120),(-35, -45)]

part8Gold = [(35, -45), (66, -4), (96, -45), (184, 70), (332, 70), (302, 30), (206, 30), (94, -120), (35, -45)]


postion1 = (0, 0)

postion2 = (0, 90)

postion3 = (-4, -4)

postion4 = (4, -4)

postion5 = (-366, 115)

postion6 = (366, 115)

postion7 = (-35, -45)

postion8 = (35, -45)


def draw_parts(part, positionGoto, fillColor):
    turtle.up()
    turtle.goto(positionGoto)
    turtle.down()
    turtle.color(fillColor)
    turtle.begin_fill()
    
    for i in range(len(part)):
        turtle.goto(part[i])
        
    turtle.end_fill()
    
    
draw_parts(part=part1Gold, positionGoto=postion1, fillColor="#f7ff00")

draw_parts(part=part2Gold, positionGoto=postion2, fillColor="#f7ff00")

draw_parts(part=part3Gold, positionGoto=postion3, fillColor="#f7ff00")

draw_parts(part=part4Gold, positionGoto=postion4, fillColor="#f7ff00")

draw_parts(part=part5Gold, positionGoto=postion5, fillColor="#f7ff00")

draw_parts(part=part6Gold, positionGoto=postion6, fillColor="#f7ff00")

draw_parts(part=part7Gold, positionGoto=postion7, fillColor="#f7ff00")

draw_parts(part=part8Gold, positionGoto=postion8, fillColor="#f7ff00")

turtle.hideturtle()
turtle.done()





from turtle import*

#we want to paint a house
shape("turtle")
#draw a square
speed(8)
width(7)
color("purple")
forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)

#end of square

#drawing a door
begin_fill()
forward(70)
color("yellow")
left(90)
forward(120)
right(90)
forward(60)
right(90)
forward(120)
end_fill()

penup()
goto(200,  200)
pendown()

color("red")
begin_fill()
right(150)
forward(200)
left(120)
forward(200)
end_fill()
#end of penup

#draw a window
penup()
goto(200, 150)
pendown()
right(60)
forward(60)
right(90)
forward(60)
right(30)
left(30)
penup()
goto(0, 200)
pendown
goto(0, 150)
right(90)
pendown()
forward(60)
left(90)
forward(50)

exitonclick()

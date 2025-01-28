from turtle import*

#we want to paint a house

#step 1: draw a square


# color - ფერი 
# forward - წინ
# right - მარჯცნივ 
# left - მარცხვნივ

# penup()
# goto()
# pendown()
width(7)
speed(30)
color("black")
forward(200)

left(90)
forward(200)
left(90)
forward(200)
left(90)
forward(200)


penup()
goto(200,200)
pendown()


right(135)
color("red")
begin_fill()
forward(150)
left(94)
forward(145)
end_fill()


penup()
goto(50, 0)
pendown()

right(139)
color("black")
begin_fill()
forward(120)
right(90)
forward(90)
right(90)
forward(120)
end_fill()
penup()
goto(200,200)
pendown()
right(90)
color("black")
forward(50)
left(90)
forward(50)
left(90)
forward(50)

penup()
goto(0,200)
pendown()
color("black")
forward(50)
right(90)
forward(50)
right(90)
forward(50)

exitonclick()
import turtle as t

# timmy_the_turtle = t.Turtle()
# timmy_the_turtle.shape("turtle")
# timmy_the_turtle.color("red")
# timmy_the_turtle.forward(100)
# timmy_the_turtle.backward(200)
# timmy_the_turtle.right(90)
# timmy_the_turtle.left(180)
# timmy_the_turtle.setheading(0)



tim = t.Turtle()

########### Challenge 2 - Draw a Dashed Line ########
for _ in range(15):
    tim.forward(10)
    tim.penup()
    tim.forward(10)
    tim.pendown()
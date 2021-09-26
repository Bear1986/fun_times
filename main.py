import turtle 
#Best practice is to place functions after an import

def square(len):
  for i in range(4):
    turtle.forward(len)
    turtle.left(90)

def rectangle(width, height):
  for i in range(2):
    turtle.forward(width)
    turtle.left(90)
    turtle.forward(height)
    turtle.left(90)


turtle.shape("turtle") # optional
turtle.speed(0) # optional
turtle.color("green")
turtle.pensize(3)

# square(90)

turtle.color("blue")
turtle.penup()
turtle.forward(100)
turtle.pendown()

#square(90)
# rectangle(90, 140)


# pritty pic

for i in range(19):
  square(90)
  turtle.right(19)
  rectangle(90, 140)

#screen to exit
turtle.Screen().exitonclick()
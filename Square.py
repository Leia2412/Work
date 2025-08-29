import turtle

screen = turtle.Screen()
screen.bgcolor("lightblue")  # You can change the background color

square_turtle = turtle.Turtle()
square_turtle.pensize(3)
square_turtle.color("darkgreen")

for _ in range(4):
    square_turtle.forward(100)  # Move forward by 100 units
    square_turtle.right(90)     # Turn right by 90 degrees

turtle.done()

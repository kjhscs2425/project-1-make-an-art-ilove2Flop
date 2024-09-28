import turtle

my_turtle = turtle.Turtle()
my_turtle.speed(300)

w = 5
for _ in range(200):
    r = 1+w
    my_turtle.circle(r+1) 
    w = r+3


x = 2
for _ in range(1000):
    y = 2+x
    my_turtle.left(140) 
    my_turtle.forward(1+y) 
    x=y+2


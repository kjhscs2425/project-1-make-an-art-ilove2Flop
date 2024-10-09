import turtle
my_turtle = turtle.Turtle()
my_turtle.speed(300)

w = 5 #W can be all real numbers
for _ in range(200):
    r = 1+w #R can be all real numbers
    my_turtle.circle(r+1) 
    w = r+3


x = 2
for _ in range(300):
    y = 2+x #Y has to be greater than x
    my_turtle.left(140) 
    my_turtle.forward(1+y) 
    x=y+2

for _ in range(100):
    def draw_spiral(size=100, angle=90):
        t = turtle.Turtle()
        t.speed(300) 

        for i in range(size):
            t.forward(i)
            t.right(angle)

    if __name__ == "__main__":
        draw_spiral()



def circular_spiral_upside_down(radius=10, step=5, rotations=10):
        t = turtle.Turtle()
        t.speed(0)  # Set the turtle's speed to the fastest
  
for i in range(rotations * 360):
    t.forward(radius)
    t.left(90)
    t.forward(step)
    t.left(90)
    radius += step

circular_spiral_upside_down()
turtle.exitonclick()

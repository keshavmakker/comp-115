import turtle

# Function to draw a square
def draw_square(t, size):
    for _ in range(4):
        t.forward(size)
        t.right(90)

# Function to draw a triangle
def draw_triangle(t, size):
    for _ in range(3):
        t.forward(size)
        t.left(120)

# Function to draw a house
def draw_house(t):
    # Drawing the outline of the house
    t.penup()
    t.goto(-100, 100)
    t.pendown()
    t.pencolor("black")  # Set pen color to black for outlining
    draw_square(t, 200)
    
    # Drawing the house
    t.penup()
    t.goto(-100, 100)
    t.pendown()
    t.begin_fill()
    draw_square(t, 200)
    t.end_fill()
    
    # Drawing the roof
    t.penup()
    t.goto(-100, 75)
    t.pendown()
    t.begin_fill()
    draw_triangle(t, 200)
    t.end_fill()

 # Drawing the church sign (plus symbol)
    t.penup()
    t.goto(0, 250)
    t.pendown()
    t.width(5)
    t.color("white")
    t.goto(0, 320)
    t.penup()
    t.goto(-20, 295)
    t.pendown()
    t.goto(20, 295)

# Function to draw a gate
def draw_gate(t):
    t.penup()
    t.goto(-25, 22)
    t.pendown()
    t.color("red")
    t.begin_fill()
    for _ in range(2):
        t.forward(50)
        t.right(90)
        t.forward(120)
        t.right(90)
    t.end_fill()

# Function to draw a window
def draw_window(t):
    t.penup()
    t.goto(0, 120)
    t.pendown()
    t.color("darkblue")
    t.begin_fill()
    t.circle(30)
    t.end_fill()

def draw_grass(t): # Function to draw grass
    t.penup()
    t.goto(-300, -200)
    t.pendown()
    t.color("lightgreen")
    t.begin_fill()
    t.goto(300, -200)
    t.goto(300, -300)
    t.goto(-300, -300)
    t.goto(-300, -200)
    t.end_fill()

def draw_flower(t, x, y, color): # Function to draw a flower
    # Drawing the stem
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.color("darkgreen")
    t.setheading(90)
    t.forward(50)
    
    # Drawing the petal
    t.color(color)
    t.begin_fill()
    t.circle(15, 180)
    t.end_fill()

# Function to draw the sun
def draw_sun(t):
    t.penup()
    t.goto(-250, 200)
    t.pendown()
    t.color("yellow")
    t.begin_fill()
    t.circle(60)
    t.end_fill()


# Main function to draw the scene
def draw_scene():
    wn = turtle.Screen()
    wn.bgcolor('sky blue')
    t = turtle.Turtle()
    t.speed(0)

    draw_house(t)
    draw_gate(t)
    draw_window(t)
    draw_grass(t)

    # Drawing flowers
    colors = ['red', 'orange', 'yellow', 'green', 'blue', 'purple', 'pink', 'cyan', 'magenta', 'violet']
    x_positions = [-250, -200, -150, -100, -50, 0, 50, 100, 150, 200]
    for i in range(10):
        draw_flower(t, x_positions[i], -220, colors[i])

    draw_sun(t)

    wn.exitonclick()

draw_scene()

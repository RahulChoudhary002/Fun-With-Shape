import turtle

def draw_polygon(sides, length, color):
    turtle.fillcolor(color)
    turtle.begin_fill()
    for _ in range(sides):
        turtle.forward(length)
        turtle.left(360 / sides)
    turtle.end_fill()

def main():
    screen = turtle.Screen()
    screen.bgcolor("lightblue")  # Set background color
    turtle.speed(3)
    
    # Draw Equilateral Triangle
    turtle.penup()
    turtle.goto(-200, 50)
    turtle.pendown()
    draw_polygon(3, 100, "yellow")
    
    # Draw Rectangle
    turtle.penup()
    turtle.goto(50, 50)
    turtle.pendown()
    turtle.fillcolor("green")
    turtle.begin_fill()
    for _ in range(2):
        turtle.forward(150)
        turtle.right(90)
        turtle.forward(80)
        turtle.right(90)
    turtle.end_fill()
    
    # Draw Hexagon
    turtle.penup()
    turtle.goto(-50, -100)
    turtle.pendown()
    draw_polygon(6, 70, "red")
    
    turtle.hideturtle()
    screen.mainloop()

if __name__ == "__main__":
    main()

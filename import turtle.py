import turtle

t = turtle.Turtle()
turtle.setup(700, 700)
t.shape("blank")
t.pensize(10)
t.penup()
t.goto(-50, 50)
t.pendown()
t.speed(1)
t.color("pink")
t.circle(20)
t.forward(30)
t.right(0)
t.left(180)
t.forward(30)
t.right(180)
t.forward(10)
colors = ["red", "green", "blue", "yellow", "orange", "black"]
for i in range(6):
    t.color(colors[i])
    t.forward(20)
    t.circle(10)
    
turtle.mainloop()
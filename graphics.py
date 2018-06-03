import turtle
import random

turtle.colormode(255)
t = turtle.Turtle()

t.speed(100)

for i in range(20):
  size = random.randint(50, 250)
  x = random.randint(-200, 200)
  y = random.randint(-200, 200)
  t.penup()
  t.goto(x, y)
  t.pendown()
  
  r = random.randint(0, 256)
  g = random.randint(0, 256)
  b = random.randint(0, 256)
  t.color(r, g, b)
  
  for i in range(50):
    t.forward(size)
    t.left(123)

for i in range(sides):
  t.forward(100)
  t.left(360/sides)
  
raw_input(" See me...")
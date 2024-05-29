#!/usr/bin/python3
import turtle


# Independence Day Philippines
# This Python code is a drawing Philippine Flag in participation to the independence day 2024 Philippines. 
# Copyright (C) 2024 Open Source Matters, Inc. All rights reserved.
# Purely written By: Michael M. Quisido III using Python Programming Language
# GNU General Public License version 2 python 3.
# For more information : info@ubuntu.com.ph or mike.quisido@ubuntu.com.ph

# Setting turtle
mikeq = turtle.Turtle()
# Setting up canvas screen
window = turtle.Screen()
# Setting up title canvas screen
window.title("Philippine Flag Drawing - Michael M. Quisido III DEMO")
# Setting up canvas screen color
window.bgcolor("#454545")
# Setting up canvas screen size
window.setup(width=1300, height=770)
# Setting up program execution speed
mikeq.speed(2)


# Heading Home
# setting up the position of the head
for kmcq1 in range(1):

# Setting up the position of the head    
    mikeq.home
    mikeq.begin_fill()
    mikeq.penup()
    mikeq.goto(-400,250)
    mikeq.pendown()
    mikeq.pen(fillcolor="#000080", pencolor="#000080", pensize=1)
    mikeq.begin_fill()
    mikeq.forward(800)
    mikeq.right(90)
    mikeq.forward(400)
    mikeq.right(90)
    mikeq.forward(800)
    mikeq.end_fill()


mikeq.penup()
mikeq.goto(-400,50)
mikeq.pendown()
mikeq.pen(fillcolor="#ff0000", pencolor="#ff0000", pensize=1)
mikeq.begin_fill()
mikeq.right(180)
mikeq.forward(800)
mikeq.right(90)
mikeq.forward(200)
mikeq.right(90)
mikeq.forward(800)
mikeq.right(90)
mikeq.forward(200)
mikeq.end_fill()


mikeq.penup()
mikeq.goto(-400,250)
mikeq.pendown()
mikeq.pen(fillcolor="#ffffff", pencolor="#ffffff", pensize=1)
mikeq.begin_fill()
mikeq.right(135)
mikeq.forward(280)
mikeq.right(90)
mikeq.forward(280)
mikeq.right(135)
mikeq.forward(390)
mikeq.end_fill()

# Star #1 The upper left quadrant of the Philippine flag within the white field of the drawing.
mikeq.begin_fill()
mikeq.penup()
mikeq.setpos(-390,220)
mikeq.pendown()
star_size = 7

extended = 1.2
patches = star_size * extended / 4

mikeq.hideturtle()
mikeq.color("#c3c300")
mikeq.shape("triangle")
mikeq.turtlesize(star_size * extended / 20)

for kmcq in range(5):
    mikeq.right(72)
    mikeq.forward(patches)
    mikeq.stamp()
    mikeq.backward(patches)
    
mikeq.end_fill() 

# Star #2 The lower left quadrant of the Philippine flag within the white field of the drawing.
mikeq.begin_fill()
mikeq.penup()
mikeq.setpos(-390,-120)
mikeq.pendown()
star_size = 7

extended = 1.2
patches = star_size * extended / 4

mikeq.hideturtle()
mikeq.color("#c3c300")
mikeq.shape("triangle")
mikeq.turtlesize(star_size * extended / 20)

for kmcq in range(5):
    mikeq.right(72)
    mikeq.forward(patches)
    mikeq.stamp()
    mikeq.backward(patches)
    
mikeq.end_fill()

# Star #3 The Philippine flag drawing features a star positioned in the center right of the white field.
mikeq.begin_fill()
mikeq.penup()
mikeq.setpos(-220,50)
mikeq.pendown()
star_size = 7

extended = 1.2
patches = star_size * extended / 4

mikeq.hideturtle()
mikeq.color("#c3c300")
mikeq.shape("triangle")
mikeq.turtlesize(star_size * extended / 20)

for kmcq in range(5):
    mikeq.right(72)
    mikeq.forward(patches)
    mikeq.stamp()
    mikeq.backward(patches)
    
mikeq.end_fill()


# The SUN #4 The center side of the white field drawning of the Philippine flag, just the center of the 3 start drawing
mikeq.penup()
mikeq.setpos((-350,0))
mikeq.pendown()
mikeq.color("#c3c300")


# executing loop 50 times 
for i in range(50):
 
        # The moving head for original is 400 units forward
        mikeq.forward(100)
        # The rotating hear for original is 844 degree right
        mikeq.left(944)
        
mikeq.end_fill()      
        
# The SUN #4 The ball part of the Sun. 
mikeq.begin_fill()
mikeq.penup()
mikeq.setpos((-307,70))
mikeq.pendown()
mikeq.pen(fillcolor="#ffff00", pencolor="#ffff00", pensize=1)
mikeq.degrees(fullcircle=360.0)
mikeq.circle(30)
mikeq.end_fill()

mikeq.hideturtle()
window.exitonclick()

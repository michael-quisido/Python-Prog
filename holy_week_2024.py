#!/usr/bin/python3

import turtle

# Holy week March 29 2024
# This Python code is a drawing of a 3 cross with a stars and a moon to participation to the holy weeek 2024
# Copyright (C) 2024 Open Source Matters, Inc. All rights reserved.
# Purely written By: Michael M. Quisido III using Python Programming Language
# GNU General Public License version 2 or later.
# For more information : info@ubuntu.com.ph or mike.quisido@ubuntu.com.ph


# set screen
mikeq = turtle.Turtle()
pywindow = turtle.Screen()
pywindow.title("Holy Week Cross on Python - By: Michael M. Quisido III")
pywindow.bgcolor("#000000")
mikeq.speed(1)

#This is to draw a 3 cross for holy week with a stars and moon on the canvas 
#Draw horizontal A
for kmcq1 in range(3):

   mikeq.penup()
   mikeq.goto(-290,-120)
   mikeq.pendown()
   mikeq.pen(fillcolor="#000080", pencolor="#000080", pensize=2) 
   
mikeq.begin_fill()
mikeq.forward(100)
mikeq.left(90)
mikeq.forward(20)
mikeq.left(270)
mikeq.backward(180)
mikeq.sety(-120)
mikeq.forward(100)  
mikeq.end_fill()


#Draw vertical  A
mikeq.penup()
mikeq.goto(-269,-120)
mikeq.pendown()
mikeq.pen(fillcolor="#000080", pencolor="#000080", pensize=2)
mikeq.begin_fill()
mikeq.setheading(90)
mikeq.forward(100)
mikeq.left(90)
mikeq.forward(20)
mikeq.left(270)
mikeq.backward(270)
mikeq.setx(-269)
mikeq.forward(270) 
mikeq.end_fill()


#Draw vertical B
mikeq.penup()
mikeq.goto(10,-120)
mikeq.pendown()
mikeq.pen(fillcolor="#000080", pencolor="#000080", pensize=2)  
mikeq.begin_fill()
mikeq.forward(100)
mikeq.left(90)
mikeq.forward(20)
mikeq.left(270)
mikeq.backward(100)
mikeq.setx(-10)
mikeq.forward(-270) 
mikeq.right(90)
mikeq.forward(21)
mikeq.end_fill()

#Draw horizontal B
mikeq.penup()
mikeq.goto(-10,-120)
mikeq.pendown()
mikeq.pen(fillcolor="#000080", pencolor="#000080", pensize=2) 
mikeq.begin_fill()
mikeq.forward(100)
mikeq.left(90)
mikeq.forward(20)
mikeq.left(270)
mikeq.backward(180)
mikeq.sety(-120)
mikeq.forward(100)  
mikeq.end_fill()


#Draw horizontal C
mikeq.penup()
mikeq.goto(269,-120)
mikeq.pendown()
mikeq.pen(fillcolor="#000080", pencolor="#000080", pensize=2)  
mikeq.begin_fill()
mikeq.forward(100)
mikeq.left(90)
mikeq.forward(20)
mikeq.left(270)
mikeq.backward(180)
mikeq.sety(-120)
mikeq.forward(100)  
mikeq.end_fill()

#Draw vertical  C
mikeq.penup()
mikeq.goto(290,-120)
mikeq.pendown()
mikeq.pen(fillcolor="#000080", pencolor="#000080", pensize=2)
mikeq.begin_fill()
mikeq.setheading(90)
mikeq.forward(100)
mikeq.left(90)
mikeq.forward(20)
mikeq.left(270)
mikeq.backward(270)
mikeq.setx(290)
mikeq.forward(270) 
mikeq.end_fill()


# Drawing star 1 pattern
mikeq.begin_fill()
mikeq.penup()
mikeq.setpos(-450,190)
mikeq.pendown()
star_size = 20

extended = 1.2
patches = star_size * extended / 4

mikeq.hideturtle()
mikeq.color("white")
mikeq.shape("triangle")
mikeq.turtlesize(star_size * extended / 20)

for kmcq in range(5):
    mikeq.right(72)
    mikeq.forward(patches)
    mikeq.stamp()
    mikeq.backward(patches)
    
mikeq.end_fill() 


# Drawing star 2 pattern
mikeq.begin_fill()
mikeq.penup()
mikeq.setpos(-390,290)
mikeq.pendown()
star_size = 10

extended = 1.2
patches = star_size * extended / 4

mikeq.hideturtle()
mikeq.color("white")
mikeq.shape("triangle")
mikeq.turtlesize(star_size * extended / 20)

for kmcq in range(5):
    mikeq.right(72)
    mikeq.forward(patches)
    mikeq.stamp()
    mikeq.backward(patches)
    
mikeq.end_fill() 


# Drawing star 3 pattern
mikeq.begin_fill()
mikeq.penup()
mikeq.setpos(-190,340)
mikeq.pendown()
star_size = 7

extended = 1.2
patches = star_size * extended / 4

mikeq.hideturtle()
mikeq.color("white")
mikeq.shape("triangle")
mikeq.turtlesize(star_size * extended / 20)

for kmcq in range(5):
    mikeq.right(72)
    mikeq.forward(patches)
    mikeq.stamp()
    mikeq.backward(patches)
    
mikeq.end_fill() 


# Drawing star 4 pattern
mikeq.begin_fill()
mikeq.penup()
mikeq.setpos(-200,200)
mikeq.pendown()
star_size = 14

extended = 1.2
patches = star_size * extended / 4

mikeq.hideturtle()
mikeq.color("white")
mikeq.shape("triangle")
mikeq.turtlesize(star_size * extended / 20)

for kmcq in range(5):
    mikeq.right(72)
    mikeq.forward(patches)
    mikeq.stamp()
    mikeq.backward(patches)
    
mikeq.end_fill() 


# Drawing star 5 pattern
mikeq.begin_fill()
mikeq.penup()
mikeq.setpos(120,290)
mikeq.pendown()
star_size = 13

extended = 1.2
patches = star_size * extended / 4

mikeq.hideturtle()
mikeq.color("white")
mikeq.shape("triangle")
mikeq.turtlesize(star_size * extended / 20)

for kmcq in range(5):
    mikeq.right(72)
    mikeq.forward(patches)
    mikeq.stamp()
    mikeq.backward(patches)
    
mikeq.end_fill() 


# Drawing star 6 pattern
mikeq.begin_fill()
mikeq.penup()
mikeq.setpos(320,210)
mikeq.pendown()
star_size = 16

extended = 1.2
patches = star_size * extended / 4

mikeq.hideturtle()
mikeq.color("white")
mikeq.shape("triangle")
mikeq.turtlesize(star_size * extended / 20)

for kmcq in range(5):
    mikeq.right(72)
    mikeq.forward(patches)
    mikeq.stamp()
    mikeq.backward(patches)
    
mikeq.end_fill() 


# Drawing moon pattern
mikeq.begin_fill()
mikeq.penup()
mikeq.goto(450,340)
mikeq.pendown()
mikeq.setheading(100)


for kmcq in range(1):

     mikeq.pen(pencolor="#ffffff", pensize=1)
     mikeq.degrees(fullcircle=360.0)
     mikeq.circle(70,360)
     mikeq.color("#ffffff")

mikeq.end_fill()

mikeq.begin_fill()
mikeq.penup()
mikeq.goto(420,360)
mikeq.pendown()
mikeq.pen(pencolor="#000000", pensize=1)
mikeq.degrees(fullcircle=360.0)
mikeq.circle(70,360)
mikeq.color("#000000") 
mikeq.end_fill()

for kmcq3 in range(1):

    mikeq.penup()
    mikeq.goto(-270,-395)
    mikeq.pendown()
    mikeq.setheading(90)
    mikeq.down()
    mikeq.pen(fillcolor="#ffffff", pencolor="#ffffff", pensize=2)
    
mikeq.begin_fill()
mikeq.write("Team: Ubuntu Philippines", align="center", font=("Ubuntu Bold", 25))
mikeq.hideturtle()
mikeq.end_fill()


pywindow.exitonclick()

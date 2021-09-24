#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 22 14:07:42 2021
@author: lillymcnichols
I chose to draw a pumpkin because this week the weather finally got cold and I am excited for Halloween!
"""
import turtle, random
from turtle import Screen
turtle.clearscreen()
#background = turtle.Turtle()
turtle.bgcolor("black")
turtle.penup()


pumpkin =  turtle.Turtle()
pumpkin.speed(10)
pumpkin.goto(0,-350)
pumpkin.color("DarkOrange1")
pumpkin.begin_fill()
pumpkin.circle(300)
pumpkin.end_fill()
pumpkin.left(180)
pumpkin.penup()

square = turtle.Turtle()
square.speed(10)
square.color("black")
square.penup()
square.goto(-150,50)
square.begin_fill()
square.pendown()
for count in range(3):
    square.forward(100)
    square.left(90)
square.end_fill()

square.penup()
square.goto(150,50)
square.begin_fill()
square.pendown()
square.setheading(90)
for count in range(3):
    square.forward(100)
    square.left(90)
square.end_fill()

stump = turtle.Turtle()
stump.speed(10)
stump.color("sienna4")
stump.penup()
stump.goto(30,290)
stump.begin_fill()
stump.pendown()
stump.setheading(180)
stump.forward(100)
stump.left(90)
stump.forward(50)
stump.left(90)
stump.forward(100)
stump.end_fill()

teeth = turtle.Turtle()
teeth.speed(10)
teeth.color("black")
teeth.penup()
teeth.goto(-200,-120)
#teeth.begin_fill()
teeth.pendown()
toothpos = -120
#teeth.setheading()
for count in range(4):
    teeth.begin_fill()
    for count in range(3):
        teeth.forward(150)
        teeth.right(120)
    teeth.end_fill()
    teeth.goto(toothpos,-120)
    toothpos = (toothpos + 80)
teeth.end_fill()

screen = Screen()
screen.colormode(255)
text = turtle.Turtle()
text.color(random.randint(1,255),random.randint(1,255),random.randint(1,255))
text.penup()
text.goto(-350,320)
text.pendown()
text.write("SPOOKY", font =("Verdana",50,"normal"))
text.penup()
text.goto(-310,265)
text.color(random.randint(1,255),random.randint(1,255),random.randint(1,255))
text.pendown()
text.write("SZN!", font=("Verdana",50,"normal"))
# I made the text color of Spooky Szn random so that every time my code is run, both "Spooky" and "Szn!" randomly choose a color excluding black because it is the background color 
turtle.done()











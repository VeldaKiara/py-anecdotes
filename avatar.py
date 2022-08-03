from tkinter import N
from turtle import *
speed(0)
bgcolor('purple')
color('lime')
hideturtle()
n = 1
p = True
while True:
    circle(n)
    if p:
        n = n - 1
    else:
         n = n + 1
    if  n==0 or n==85:
        p=not p
    right(1.6)
    backward(5)





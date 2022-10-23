from cmath import cos
from decimal import ROUND_DOWN
import math
import sys
import numpy

pi = math.pi

def round_down(n, decimals=0):
    multiplier = 10 ** decimals
    return math.floor(n * multiplier) / multiplier


def pizzanum(fatias, raio):
    r = int(raio)

    b = math.radians((360/int(fatias))*0.5)
    cossenus = cos(b).real
    profundidade = round(r - (cossenus * r), 3)

    senus = math.sin(b).real
    comprimento = round(2 * senus * r, 2)
    print(comprimento)

pizzanum(int(sys.argv[1]), int(sys.argv[2]))



#b = round_down(math.radians(60), 4)
#print(2 * pi)
#comp = cos(math.radians(60))
#print(round_down(comp.real, 2))




""" from tkinter import *

def printSomething():
    # if you want the button to disappear:
    # button.destroy() or button.pack_forget()
    label = Label(t, text= str(pizzanum(int(sys.argv[1]), int(sys.argv[2]))))
    #this creates a new label to the t
    label.pack() 

t = Tk()

button = Button(t, text="Calcular", command=printSomething) 
button.pack()
t.geometry('400x250')
t.mainloop()

 """

import turtle
s = turtle.getscreen()
t = turtle.Turtle()

radiuss = 100

# move
turtle.penup()
turtle.right(90)
turtle.forward(radiuss)
turtle.left(90)
turtle.pendown()

turtle.circle(radiuss)

# move back
turtle.penup()
turtle.right(-90)
turtle.forward(radiuss)
turtle.left(-90)
t.goto()



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

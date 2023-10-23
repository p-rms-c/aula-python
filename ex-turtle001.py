from turtle import *

speed(4)

def poligonos(n):
    for count in range(n):
        forward(10)
        left(360 / n)

def write_trilha():
    for count in range(30):
        forward(5)
        penup()
        forward(5)
        pendown()


#chame aqui a função desejada
poligonos(30)

done()
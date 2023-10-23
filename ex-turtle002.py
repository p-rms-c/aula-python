from turtle import *
speed(200)

def casa():
    forward(200)
    left(90)
    forward(100)
    left(45)
    forward(140)
    left(90)
    forward(140)
    left(45)
    forward(100)
    left(90)
    penup()
    forward(40)
    pendown()
    left(90)
    forward(70)
    right(90)
    forward(30)
    right(90)
    forward(70)
    penup()
    backward(35)
    left(90)
    forward(50)
    pendown()
    for count in range(2):
        forward(40)
        left(90)
        forward(30)
        left(90)

def estrela():
    right(110)
    for count in range(5):
        forward(200)
        left(144)
    
def flor():
    left(90)
    for count in range(60):            
        forward(3)
        right(1.5)
    
    for count in range(60):             
        forward(3)
        left(1.5)
    
    left(90)

    for count in range(2):
        for count in range(60):            
            forward(3)
            left(1.5)

    left(90)

    for count in range(60):            
        forward(3)
        left(1.5)

    for count in range(60):            
        forward(3)
        right(1.5)

    right(90)

    for count in range(60):            
        forward(3)
        right(1.5)

    left(45)

    for count in range(60):            
        forward(3)
        left(1.5)

    left(90)

    for count in range(60):            
        forward(3)
        left(1.5)

    right(180)

    for count in range(60):            
        forward(3)
        left(1.5)

    left(90)

    for count in range(60):            
        forward(3)
        left(1.5)

    left(180)

    for count in range(60):            
        forward(3)
        left(1.5)

    left(90)

    for count in range(60):            
        forward(3)
        left(1.5)

    right(90)

    for count in range(60):            
        forward(3)
        right(1.5)

    right(90)

    for count in range(60):            
        forward(3)
        right(1.5)

    right(135)

    for count in range(60):            
        forward(3)
        right(1.5)
# a flor deu trabalho

flor()

done()
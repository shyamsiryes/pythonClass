from turtle import *


def square(lenght):
    i=0
    while i<4:
        forward(lenght)
        left(90)
        i=i+1
square(200)


def polygon(lenght, sides):


    i=0
    while i<sides:
        forward(lenght)
        left(360/sides)
        i=i+1
polygon(200,10)

i=0

s= int(input("enter number of sides: "))
polygon(5,s)
done()

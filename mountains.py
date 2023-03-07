from turtle import *
i=1
pendown()
pensize(0.0000000000000000000000000001)
color("red", "aqua")
begin_fill()
while True:
    forward(200)
    left(181)
    i=i+1
    if abs(pos())<1:
        break


end_fill()
penup()
goto(-100, -100)

penup()
color("black", "brown")
begin_fill()

i=0
while i < 3:
    forward(200)
    left(120)
    i=i+1
end_fill()

done()
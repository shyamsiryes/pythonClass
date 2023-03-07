from turtle import *
i=1
pendown()
pensize(0.0000000000000000000000000001)
color("red", "aqua")
begin_fill()
while True:
    forward(200)
    left(124)
    i=i+1
    if abs(pos())<1:
        break

end_fill()
done()
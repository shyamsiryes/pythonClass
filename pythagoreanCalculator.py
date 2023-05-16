from math import sqrt
print('Assume the sides of you triange are a(leg),b(leg), and c(hypotneuse)')
#a = int(input('Enter side lenghth a: '))
#b = int(input('Enter side length b:  '))
#c = int(input(' Enter side length c: '))
formula = input(' Do you want to calculate side a,b, or c')

if formula == 'c':
    a=float(input('Enter side lenghth a: '))
    b=float(input('Enter side length b:  '))
    hyp = sqrt(a * a + b * b)
    print(f' Your Hypotneuse is {hyp}')

if formula == 'b':
    a = float(input('Enter side lenghth a: '))
    c = float(input('Enter side length c:  '))
    Leg_2 = sqrt(c*c-a*a)
    print(f' Your Missing Leg is {Leg_2}')

if formula == 'a':
    b = float(input('Enter side lenghth b: '))
    c = float(input('Enter side length c:  '))
    Leg_1 = sqrt(c*c-b*b)
    print(f' Your Missing Leg is {Leg_1}')





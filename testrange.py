guess = int(input('Pick Any Real Number'))
choice = int(input("Type 1 if you want me to count all numbers from o to your number, type 2 if you want all even numbers to your number, type 3 if you want a list of all odd numbers up to your number"))
if choice==1:
    v = list(range(0, guess, 1))
    print(v)
if choice==2:
    b = list(range(0, guess, 2 ))
    print(b)
if choice==3:
    f = list(range(1, guess, 2 ))
    print(f)

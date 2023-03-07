#is it prime number
num = int(input("Enter any Real Number: "))
counter = 2
isPrime= True
while counter< num:
    if num % counter == 0:
        isPrime=False


        break
    else:
        counter = counter + 1
if isPrime:
    print (" This is  prime number")
else:
    print('This is composite number')
    break





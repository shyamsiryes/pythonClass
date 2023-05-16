ran = int(input("Enter any Real Number: "))
x=list(range(1, ran))

counter = 2
isPrime= True
while counter< ran:
    if ran % counter == 0:
        isPrime=False


        break
    else:
        counter = counter + 1

sum=0
for num in x:
    #sum = sum + isPrime
  #  print('The sum of all the prime numbers up to your numbers is: ')
  #  print(sum)
    counter = 2
    isPrime = True
    while counter < ran:
        if ran % counter == 0:
            isPrime = False

            break
        else:
            counter = counter + 1
            for d in x:
                sum = 0
                sum = sum + isPrime
            print(sum)
    



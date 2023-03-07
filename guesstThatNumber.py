import random

num= random.randint(1, 9)
counter = 0
guess = False
while not guess:
    userNum = int(input(" Guess the number between 1 and 9, You only have 2 guesses: "))
    if userNum == num:
        print('You guessed it right!')
        break
    elif userNum < num:
        print('Too Low!')


    else:
        print (' Too High ')


    counter=counter+1
    if counter==2:
        print('You lost')
        break
import random
# Rock Paper Scissors Game with computer
while True:
    user= input("Enter 'r' for Rock, 'p' for Paper, and 's' for scissors; ")

    computer = random.choice(['r','p','s'])

# Paper is better than Rock, Rock is better than Scissors, Scissors is better than Paper

    if user == 'r' and computer == 's':
        print("Computer chose scissors, you won!")
    elif user == 'p' and computer == 'r':
        print('Computer selected paper, you won!')
    elif user== 's' and computer == "p":
        print(' Computer chose paper, you won')
    elif user == 'r'and computer =='p':
        print(' computer chose paper, you lost')
    elif user == 'p'and computer =='s':
        print(' computer chose scissors, you lost')
    elif user == 's'and computer =='r':
        print(' computer chose rock, you lost')
    elif user == "s" and computer == 's':
        print('Computer chose scissors, you tied')
    elif user == "r" and computer == 'r':
        print('Computer chose rock, you tied')
    elif user == 'p' and computer == 'p':
        print('Computer chose paper, you tied')


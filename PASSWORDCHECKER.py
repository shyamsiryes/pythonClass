username = input('Enter Your Name')
password = input('Enter Your Password: ')
numberOfCharacters = len(password)
while numberOfCharacters < 8:
    print(" Password should be at least 8 characters long")
    password = input(" Enter your password: ")
    numberOfCharacters = len(password)
hiddenPassword = '*' * len(password)
print(f"Hello {username} your password is {hiddenPassword}")
revealPassword = input('Do You Want to See you password (enter yes or no)')
if revealPassword == 'yes':
    print(f" Your password is {password}")
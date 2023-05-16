n=input('What is Your Name: ')
z=int(input('What is Your Zip Code: '))
a=int(input('What is Your Age: '))
strlist=[n,z, a]
print(strlist)
if a<=11 and a>=17:
    print('You are in middle school')
elif a>=18 and a<=22:
    print('You are in College')
elif a>=5 and a<=11:
    print('You are in Elementary School')
else:
    print('Get ready for your first day of primary school')



user = int(input('Pick any number'))
zed = list(range(1, user))
for num in zed:
    print(num)



zed2= list(range(1,user,2))
for bit in zed2:
    print(bit)

zed3 = list(range(0,user,2))
for zit in zed3:
    print(zit)
su = 0
lists = list(range(0,user+1))
for git in lists:
    su = su +git
print(su)

print(f'Your odd numbers are {zed2}')
print(f'Your even numbers are {zed3}')









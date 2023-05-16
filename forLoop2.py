
user = int(input('pick any numnber'))
lists = list(range(1,user+1))
sum = 1
for num in lists:
    sum = sum *num

print(sum)
print(f'The factorial of your number is {sum}. ')

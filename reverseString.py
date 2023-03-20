#code to reverse any string
def reverseString(str):
   counter = len(str) -1
   rev=""
   while counter  >= 0:
       rev = rev +str[counter]
       counter = counter - 1
       #this is the code that evealuates the string that was inputed

   return rev
name = input("enter your name: ")
print(f'This is your name spelled backwards: {reverseString(name)}')
if name==reverseString(name):
    print('Your name is a palindrome')
else:#this code evaluates if the string inputed was a palindrome or not
    print('Nice Name')



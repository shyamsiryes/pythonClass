name=input("Enter Your 3 favorite fruit: ")
strList = ["Hello" , name ,    "good choice"]
#name = 'planet'
print(name[0])
print(name[1])
print(name[2])
print(''.join(strList))
counter=0
while counter <len(name):
    print (name[counter])
    counter = counter +1

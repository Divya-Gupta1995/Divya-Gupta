#write a python program that accept a word from the user and reverse it

str1= str(input("Enter Any word"))
length=len(str1)
rev=""

while length>0:
    rev=rev+str1[length-1]
    length-=1

print(rev)




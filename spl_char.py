#Program to check if a string contains any special character.
'''
Sample Input :
Python is a high level programming language

Sample Output :
String is accepted

Sample Input :
Python@is a&high level*programming language

Sample Output :
String is not accepted
'''

str=input("Enter a string")
spl=str.split()
for i in spl:
    for j in i:
        if j.isalnum() or j==" ":
            n=True
        else:
            n=False
            print("This string is not acceptable")
            break
    if n==False:
        break
if n==True:
    print("String is acceptable")


    




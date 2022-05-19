'''
str=input("Enter a string")
spl=str.split()
print(spl)
for i in spl:
    if any(not c.isalnum() for c in str):
        print("String is not acceptable")
        break
    else:
        print("String is acceptable")
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


    




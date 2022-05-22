tup=[]
size= int(input("Enter the size of your tuple"))
add=True
# for i in range(size):
#         tup=[]
#         temp=int(input("enter your element"))
#         tup.append(temp)

lst=[]
while add==True:
    for i in range(0,size):
        tup=[]
        temp=int(input("enter your element"))
        tup.append(temp)
    
    print(tup)
    
    lst=[].extend(tup)
    add=bool(input("Do you wish to add one more tuple"))
    if add!=True:
        break
    

print(lst)

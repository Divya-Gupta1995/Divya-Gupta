tup=[]
size=int(input("enter the size of tuple"))
add_ele='y'
lst=[]
while add_ele=='y':
    for i in range(0,size):
        tup=list(tup)
        temp=int(input("enter the element"))
        tup.append(temp)

    tup=tuple(tup)
    lst.append(tup)
    tup=[]
    add_ele=input("enter 'y' to add one more tuple")
    if add_ele!="y":
        break

print("list of tuples:",lst)

#sorting list of tuples on the basis of last elements of tuple
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

print("original list:",lst)

for i in range(0,len(lst)):
    for j in range(i+1,len(lst)):
        one=lst[i][len(lst[i])-1]
        two=lst[j][len(lst[j])-1]
        if one>two:
            lst[i],lst[j]=lst[j],lst[i]

print("sorted list:",lst)




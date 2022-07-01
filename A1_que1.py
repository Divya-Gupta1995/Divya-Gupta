#Python program to get the fibonacci series between 0 to 50

a=0
b=1
c=a+b
print(a,b,end=" ")


while c<50:
    print(c,end=" ")
    a=b
    b=c
    c=a+b




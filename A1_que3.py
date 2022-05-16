#Write a python program to count the number of even and odd numbers from a series of numbers.


lst=[]      #Defining empty list
n=int(input("Enter the number of elements for list"))   #Asking for number of elements in list
print("Enter the numbers",end="   ")

for i in range(0,n):
    ele=int(input())
    lst.append(ele)


count_even=0
count_odd=0

for i in range(0,n):
    if lst[i]%2==0:
        count_even=count_even+1
    else:
        count_odd=count_odd+1

print("you have entered",count_even,"even numbers")
print("you have entered",count_odd,"odd numbers")


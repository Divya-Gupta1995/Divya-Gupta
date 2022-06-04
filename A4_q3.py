# Write a Python program to square the elements of a list using map() function.

# Sample List: [4, 5, 2, 9]

# Square the elements of the list:

# [16, 25, 4, 81]
lst=[]  #Taking input of list from user
size=int(input("Enter the size of your list"))
for i in range(size):
    print("enter the value")
    ele=int(input())
    lst.append(ele)

print("Your list:",lst)

square=list(map(lambda x:x**2,lst))  #using map and lambda function for finding square of list
print("Square of list numbers:",square)


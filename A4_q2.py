# Write a Python program to triple all numbers of a given list of integers. Use Python map.

# sample list: [1, 2, 3, 4, 5, 6, 7]

# Triple of list numbers:
# [3, 6, 9, 12, 15, 18, 21]

lst=[]  #Taking input of list from user
size=int(input("Enter the size of your list"))
for i in range(size):
    print("enter the value")
    ele=int(input())
    lst.append(ele)

print("Your list:",lst)

triple=list(map(lambda x:x*3,lst))  #using map and lambda function for finding triple of list
print("Triple of list numbers:",triple)
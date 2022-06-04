# Write a Python program to create a lambda function that adds 25 to a given number passed in as an argument.

# sample input: 10

# sample output: 35

n=int(input("Enter the number"))
add=lambda x:x+25
print("Adding the entered no. with 25, Result:",add(n))
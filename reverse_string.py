# Write a Python program to reverse a string.

'''
Sample String : "1234abcd"

Expected Output : "dcba4321
'''
def rev_str():    

    str=input("enter a string")
    rev=""
    global len
    len=len(str)
    for i in range(len-1,-1,-1):
        j=str[i]
        rev=rev+j

    print("reverse of this string is:",rev)
    
rev_str()

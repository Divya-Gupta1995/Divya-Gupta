# Write a Python function that accepts a string and calculate the number of upper case letters and lower case letters.

'''
Sample String : 'The quick Brow Fox'

Expected Output :

No. of Upper case characters : 3

No. of Lower case Characters : 12
'''
def case_count(str,len):
    global upper_case_count
    global lower_case_count
    upper_case_count=0
    lower_case_count=0
    for i in range(0,len):
        if str[i].isupper()==True:
            upper_case_count+=1
        else:
            lower_case_count+=1
    

    print("total upper case letters:",upper_case_count)
    print("total lower case letters:",lower_case_count)

str=input("Enter a string")
len=len(str)
case_count(str,len)

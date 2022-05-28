# Write a Python function to sum all the numbers in a list.
'''
Sample List : (8, 2, 3, 0, 7)

Expected Output : 20

Explanation:

Summation should like 8+2+3+0+7 = 20
'''

def lst_input():
    lst=[]
    size=int(input("enter the size of your list"))
    for i in range(size):
        data=int(input("enter the number"))
        lst.append(data)

    return lst


def sum_lst(lst):
    sum=0
    for i in range(0,len(lst)):
        sum=sum+lst[i]
    return sum

lst=lst_input()
print("list:",lst)
sum=sum_lst(lst)
print("sum of all elements of list:",sum)



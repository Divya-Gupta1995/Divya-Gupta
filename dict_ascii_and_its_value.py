#Write a Python program to print a dictionary whose keys should be the alphabet from a-z and the value should be corresponding ASCII values

key=[]
value=[]
i=ord('a')
j=chr(i)
for i in range(ord('a'),ord('z')+1):
    j=chr(i)
    key.append(i)
    value.append(j)

dict=dict(zip(key,value))
print(dict)

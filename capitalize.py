#Python program to capitalize the first and last character of each word in a string (input string should be a statement)
'''
Sample Input :

Python is a high level programming language
Sample Output :

PythoN IS A HigH LeveL ProgramminG LanguagE
'''

str=input("Please write a sentence")
spl=str.split()
join=""
for i in spl:
    if len(i)>1:
        i = i[0:1].upper() + i[1:len(i)-1] + i[len(i)-1:len(i)].upper()
    else:
        i=i[0:1].upper()

    join=join+" "+i

print(join)
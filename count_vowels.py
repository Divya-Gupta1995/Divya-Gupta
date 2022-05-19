s=input("Enter a sentence")
t=s.split()
vowels=0
for i in t:
    for j in i:
        if j=="a" or j=="e" or j=="i" or j=="o" or j=="u" or j=="A" or j=="E" or j=="I" or j=="O" or j=="U":
            vowels=vowels+1

print("Total numbers of vowels in the above statement:",vowels)

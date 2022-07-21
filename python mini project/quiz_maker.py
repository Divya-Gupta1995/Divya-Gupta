
from json import*
import random

file=open("quiz.json")
data=load(file)
l=list(data.keys())
option=['A','B','C','D']
random.shuffle(l)
score=0
print("Welcome to the quiz game")
print("GENERAL INSTRUCTIONS TO PLAY QUIZ GAME:: you will be provided, a set of questions along with 4 options")
print("you have to select an option (A/B/C/D),for each right answer you will be rewarded 1 point and your total score will be displayed at the end of quiz  ")
print("BEST OF LUCK!!!")
print("Press 1 to start the quiz")
cntn=0
total=0
cntn=int(input())
if cntn==1:

    for i in l:
        total+=1
        print(i)
        options=list(data[i].split(","))
        choice=options[:]
        random.shuffle(choice)
        opt=dict(zip(option,choice))
        for k,v in opt.items():
            print(k,"   ",v)
        
        ans=input("Enter your answer:")
        if opt[ans]==options[0]:
            score+=1
            print("Congratulations!!It is a correct answer") 
        else:
            print("Oops!!!Wrong Answer")

    print("Congratulations,, your total score is",score,"out of",total)

        
        


    





    
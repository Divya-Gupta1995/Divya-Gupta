lst=list[input("Enter some numbers")]
even=0
odd=0

for i in range(lst):
    lst[i]=int
    if lst[i]%2==0:
        even=even+1
    else:
        odd=odd+1
print("Even numbers:",even)
print("Odd numbers:",odd)


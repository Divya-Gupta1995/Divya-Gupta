# Write a Python class to implement power(x, n)

# Sample Input:
# x: 10
# n: 2
# Sample Output:
# 100

class exponential():
    
    def __init__(self):
        self.number=int()
        self.power=int()
        self.result=int()

    def pow(self):
        self.number=int(input("Enter the number"))
        self.power=int(input("Enter the power"))
        self.result=self.number**self.power  
        return self.result

    def display(self):
        print(f"{self.number} raise to the power {self.power} = {self.result}")


if __name__=="__main__":
    obj=exponential()
    obj.pow()
    obj.display()
    


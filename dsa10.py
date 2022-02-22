#Q10. Write a program to find the smallest number using a stack.

class stack():
    def __init__(self):
        self.items=[]
    def isEmpty(self):
        return self.items==[]
   
    def push(self):
         n=int(input('How many numbers are there in a list: '))
         for i in range(n):
             a=int(input('enter number: '))
             self.items.append(a)
    def display(self):
        return self.items
    def smallest(self):
        return min(self.items)
s=stack()
s.push()

print(s.display())
print(s.smallest())


    
       
    

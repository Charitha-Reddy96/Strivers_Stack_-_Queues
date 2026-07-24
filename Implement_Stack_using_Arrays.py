
class stack:
    def __init__(self,size_of_array):
        self.stck = []
        self.size_of_array = size_of_array
    def push(self,num):
        if len(self.stck) < self.size_of_array:
            self.stck.append(num)
        else:
            print("Stack is full")
    def pop(self):
        if len(self.stck) == 0:
            print("Stack is underflow")
        else:
            self.stck.pop()
    def size_stack(self):
        print(f"Size of the stack :{len(self.stck)}")
    
    def top(self):
        if len(self.stck) > 0:            
            print(f"Top element is: {self.stck[-1]}")
        else:
            print("Stack is empty")
    def display(self):
        if len(self.stck) == 0:
            print("Stack is Empty")
        else:
            print(self.stck)

s = stack(5)
s.push(1)
s.push(2)
s.push(3)
s.push(4)
s.display()
s.top()
s.size_stack()
s.pop()
s.pop()
s.push(7)
s.display()
s.top()
s.size_stack()
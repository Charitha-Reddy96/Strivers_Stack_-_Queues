class Stack:
    def  __init__(self):
        self.stk = []
        self.top = -1
    def push(self,data):
        if self.top == -1:
            self.stk.append(data)
            self.top = 0
        else:
            li = []
            li.extend(self.stk)
            self.stk.clear()
            self.stk.append(data)
            self.stk.extend(li)
            self.top += 1
    
    def pop(self):
        if self.top == -1:
            print("Stack is empty to POP")   
        else:
            self.stk.pop()
            self.top -= 1   
              
    def display(self):
        if self.top == -1:
            print("Stack is empty to Display elements")
        else:
            print("The Stack : ",self.stk)
            
    def top_element(self):
        if self.top == -1:
            print("Stack is empty")
        else:
            print("The Top element is : ",self.stk[self.top])
        
    
        
s = Stack()
s.push(1)
s.push(2)
s.push(3)
s.push(4)
s.display()
s.pop()
s.display()
s.pop()
s.display()
s.top_element()
             
        
    


class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
class Stack:
    def __init__(self):
        self.head = None
        self.top = None
        self.size = 0
    
    def push(self,num):
        if self.head == None:
            temp = Node(num)
            self.head = self.top = temp     
        else:
            temp = Node(num)
            self.top.next = temp
            self.top= temp
        self.size += 1
        
    def pop(self):
        if self.head == None:
            print("Stack is empty")
            return None
        if self.head == self.top:
            self.head = self.top = None
        else:
            previous = self.head
            while previous.next != self.top:
                previous = previous.next
            previous.next = None
            self.top = previous
        self.size -= 1
    
    def top_element(self):
        if self.head is None:
            print("Stack is empty")
        else:
            print(f"Top Element is : {self.top.data}")
            
    def size_stack(self):
        print(f"Size of the Stack : {self.size}")
        
    def display(self):
        if self.head is None:
            print("Stack is empty")
        else:
            temp = self.head
            while temp is not None:
                print(temp.data, end=" -> " if temp.next else "")
                temp = temp.next
            print()

s = Stack()
s.push(1)
s.push(2)
s.push(3)
s.push(4)
s.display()
s.top_element()
s.size_stack()  
s.pop()
s.pop()
s.display()
s.top_element()
s.size_stack() 
s.pop()
s.pop()
s.size_stack()
s.pop()  # Attempt to pop from an empty stack

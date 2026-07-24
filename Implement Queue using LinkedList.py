class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Queue:
    def __init__(self):
        self.front = None
        self.rear = None
        self.size = 0
    
    def enqueue(self, data):
        new_node = Node(data)
        if self.rear is None:
            self.front = self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node
        self.size += 1

    def dequeue(self):
        if self.front is None:
            print("Queue is empty")
        else:
            self.front = self.front.next
            if self.front is None:
                self.rear = None
            self.size -= 1

    def display(self):
        if self.front is None:
            print("Queue is empty")
        else:
            temp = self.front
            while temp is not None:
                print(temp.data, end=" -> " if temp.next else "")
                temp = temp.next
            print()

    def size_queue(self):
        print(f"Size of the queue : {self.size}")
        
    def peek(self):
        if self.front is None:
            print("Queue is empty")
        else:
            print(f"Front element is : {self.front.data}")

q = Queue()
q.enqueue(10)
q.enqueue(20)
q.enqueue(30)
q.display()  # Output: 10 -> 20 -> 30
q.dequeue()
q.display()  # Output: 20 -> 30
q.size_queue()  # Output: Size of the queue : 2
q.peek()  # Output: Front element is : 20
q.dequeue()
q.dequeue()
q.dequeue()  # Output: Queue is empty
q.size_queue()  # Output: Size of the queue : 0
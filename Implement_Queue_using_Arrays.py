class Queue:
    def __init__(self, size_of_array):
        self.que = [None] * size_of_array
        self.size_of_array = size_of_array
        self.start = self.end = -1
        self.current_size = 0

    def enqueue(self, num):
        if self.current_size < self.size_of_array:
            if self.start == -1:
                self.start = self.end = 0
            else:
                self.end = (self.end + 1) % self.size_of_array
            self.que[self.end] = num
            self.current_size += 1
        else:
            print("Queue is Full")
    def dequeue(self):
        if self.current_size == 0:
            print("Queue is empty")
            return None
        self.que[self.start] = None
        self.current_size -= 1
        if self.current_size == 0:
            self.start = self.end = -1
        else:
            self.start = (self.start + 1) % self.size_of_array

    def size_queue(self):
        print(f"Size of the Queue :{self.current_size}")

    def top(self):
        if self.current_size == 0:
            print("Queue is empty")
        else:
            print(self.que[self.start])

    def display(self):
        if self.current_size == 0:
            print("Queue is Empty")
            return
        items = []
        index = self.start
        for _ in range(self.current_size):
            items.append(self.que[index])
            index = (index + 1) % self.size_of_array
        print(items)


q = Queue(5)
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
q.enqueue(4)
q.display()
q.top()
q.dequeue()
q.dequeue()
q.display()
q.top()
q.size_queue()
q.enqueue(7)
q.enqueue(5)
q.dequeue()
q.dequeue()
q.dequeue()
q.display()
q.top()
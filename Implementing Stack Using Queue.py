from collections import deque

class StackUsingQueue:
    """A stack implemented with one queue.

    The most recently inserted item is kept at the front of the queue, so a
    pop operation is always a simple removal from the front.
    """

    def __init__(self):
        self.queue = deque()

    def enqueue(self, data):
        """Push an item onto the stack (kept for the original API)."""
        self.queue.append(data)
        for _ in range(len(self.queue) - 1):
            self.queue.append(self.queue.popleft())

    def dequeue(self):
        """Pop and return the item at the top of the stack."""
        if not self.queue:
            print("Stack is underflow")
            return None

        pop_num = self.queue.popleft()
        print("Deleted element :", pop_num)
        return pop_num

    # Conventional stack method names.
    push = enqueue
    pop = dequeue

    def display(self):
        if not self.queue:
            print("Stack is empty")
        else:
            print("The Stack : ", list(self.queue))


s = StackUsingQueue()
s.enqueue(1)
s.enqueue(2)
s.enqueue(3)
s.display()
s.dequeue()
s.display()
s.enqueue(4)
s.dequeue()
s.dequeue()

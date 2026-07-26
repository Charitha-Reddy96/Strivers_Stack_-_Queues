class QueueUsingStacks:
    """A FIFO queue implemented with two stacks."""

    def __init__(self):
        self._input_stack = []
        self._output_stack = []

    def _move_to_output(self):
        """Move items only when the front of the queue is needed."""
        if not self._output_stack:
            while self._input_stack:
                self._output_stack.append(self._input_stack.pop())

    def enqueue(self, data):
        self._input_stack.append(data)

    def dequeue(self):
        self._move_to_output()
        if not self._output_stack:
            print("Queue is empty")
            return None
        return self._output_stack.pop()

    def peek(self):
        self._move_to_output()
        if not self._output_stack:
            print("Queue is empty")
            return None
        return self._output_stack[-1]

    def display(self):
        if not self._input_stack and not self._output_stack:
            print("Queue is empty")
            return

        # The output stack's top is the queue front.
        items = list(reversed(self._output_stack)) + self._input_stack
        print("Queue:", *items)

    def size(self):
        return len(self._input_stack) + len(self._output_stack)

    # Names used by the original example.
    push = enqueue
    pop = dequeue
    top_element = peek


# Backward-compatible name for code that used the original class name.
Stack = QueueUsingStacks


q = QueueUsingStacks()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
q.enqueue(4)
q.display()
print("Deleted element:", q.dequeue())
q.display()
print("Front element:", q.peek())

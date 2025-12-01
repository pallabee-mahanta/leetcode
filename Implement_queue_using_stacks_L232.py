class MyQueue:

    def __init__(self):
        self.in_stack = []  # Used for pushing new elements (enqueue)
        self.out_stack = []  # Used for popping elements (dequeue)

    def push(self, x: int) -> None:
        """
        Pushes element x to the back of the queue.
        """
        self.in_stack.append(x)

    def pop(self) -> int:
        self.peek()  # Ensure output stack has the current front/not empty
        return self.out_stack.pop()

    def peek(self) -> int:
        if not self.out_stack:  # Transfer elements if output stack is empty
            while self.in_stack:
                self.out_stack.append(self.in_stack.pop())
        return self.out_stack[-1]

    def empty(self) -> bool:
        return not self.in_stack and not self.out_stack


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()

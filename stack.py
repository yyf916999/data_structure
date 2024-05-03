class Stack:
    def __init__(self):
        self.stack = []

    def push(self,value):
        self.stack.append(value)
    
    def pop(self):
        return self.stack.pop()

    def peek(self):
        return self.stack[-1]
    
    def print(self):
        print(self.stack)
stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)

print(stack.peek())
stack.pop()
stack.print()
class Stack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if not self.is_empty():
            return self.stack.pop()
        return None

    def peek(self):
        if not self.is_empty():
            return self.stack[-1]
        return None

    def is_empty(self):
        return len(self.stack) == 0

    def print_stack(self):
        print("Stack:", self.stack)

if __name__ == "__main__":
    stack = Stack()
    stack.push(1)
    stack.push(2)
    stack.push(3)
    print("Original stack:")
    stack.print_stack()
    stack.pop()
    print("Stack after popping an element:")
    stack.print_stack()
    print("Top element:", stack.peek())
class Stack(object):
    def __init__(self):
        self.count = 0
        self.data = 0
        self.stack = []

    # O(1)
    def push(self, data):
        self.stack.append(data)
        self.count += 1

    # O(1)
    def pop(self):
        if self.count == 0:
            print("Stack is empty")
        else:
            del self.stack[0]

            if self.count < 0:
                self.count = 0
            else:
                self.count -= 1

    # O(n)
    def traverse(self):
        print(self.stack)
        return

    # O(n)
    def is_in_stack(self, data):
        if self.count == 0:
            print("Stack is empty")
            return
        else:
            for i in self.stack:
                if i == data:
                    print ("%s is in the Stack" % data)
                    return
                elif self.count == 0:
                    print("Stack is empty")
                    return

        print("%s was nto found in the stack" % data)

    # O(1)
    def stack_size(self):
        return self.count

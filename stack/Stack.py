from stack.Node import Node

class Stack(object):
    def __init__(self):
        self.head = Node(None)
        self.data = 0
        self.count = 0

    # O(1) - Not working correctly, using first node as head
    def push(self, data):
        newNode = Node(data)

        if self.count == 0:
            self.head.nextNode = newNode
        else:
            newNode.nextNode = self.head.nextNode
            self.head.nextNode = newNode

        self.count += 1

    # O(1)
    def pop(self):
        if self.count == 0:
            print("stack is empty")

        elif self.count == 1:
            del self.head
            self.count -= 1

        else:
            newNode = self.head.nextNode
            self.head.nextNode = newNode.nextNode
            del newNode
            self.count -= 1


    # O(n)
    def traverse(self):
        if self.head:
            while self.head:
                print (self.head.data)
                self.head = self.head.nextNode
        else:
            print("Stack is empty")

    # O(1)
    def stack_size(self):
        print ("There are %d items in the stack " % self.count)

    # 0(n)
    def is_in_stack(self, data):

        if self.count == 0 :
            print ("stack is empty")

        elif self.head == None:
            print ("%s was not in the list" % data)

        else:
            if self.head.data == data:
                print ("%s was found in the stack" % self.head.data)
            else:
                self.head = self.head.nextNode
                self.is_in_stack(data)

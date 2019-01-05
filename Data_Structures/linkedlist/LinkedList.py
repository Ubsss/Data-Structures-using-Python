from Data_Structures.linkedlist.Node import Node

class LinkedList(object):
    def __init__(self):
        self.head = None
        self.counter = 0

    # With O(1) -- Constant time complexity
    def insert_at_start(self, data):
        newNode = Node(data)

        if not self.head:
            self.head = newNode
        else:
            newNode.nextNode = self.head
            self.head = newNode

        self.counter += 1

    # O(1) -- constant time complexity
    def list_size(self):
        return self.counter

    # O(n) - linear time complexity
    def print_list(self):

        while self.head:
            print (self.head.data)
            self.head = self.head.nextNode


    # O(n) -- linear time complexity
    def insert_at_end(self, data):

        if self.head is None:
            self.insert_at_start(data)
            return

        self.counter += 1

        newNode = Node(data)
        actualNode = self.head

        while actualNode.nextNode is not None:
            actualNode = actualNode.nextNode

        actualNode.nextNode = newNode

    # O(n) - linear time complexity if value is not head
    def remove(self, data):

        if self.head:
            if data == self.head.data:
                del data
                self.head = self.head.nextNode
            else:
                self.head.remove(data, self.head)

        self.counter -= 1

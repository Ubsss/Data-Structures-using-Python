from Data_Structures.queueDS.Node import Node

class Queue(object):

    def __init__(self):
        self.count = 0
        self.head = None
        self.data = 0

    # O(1)
    def enqueue(self, data):
        newNode = Node(data)

        if self.head is None:
            self.head = newNode
        else:
            newNode.nextNode = self.head.nextNode
            self.head.nextNode = newNode
        self.count += 1

    # O(1)
    def dequeue(self):
        if not self.head:
            print("Queue is empty")
        else:
            newNode = self.head
            self.head = newNode.nextNode
            del newNode
            self.count -= 1

    # O(n)
    def traverse(self):
        while self.head:
            print(self.head.data)
            self.head = self.head.nextNode

    # O(1)
    def queue_size(self):
        print (self.count)

    # O(n)
    def is_in_queue(self, data):
        if self.count == 0:
            print ("Queue is empty")
        elif self.head == None:
            print ("%s is not in queue" % data)
        else:
            if self.head.data == data:
                print ("%s was found in the list" % self.head.data)
                return True
            else:
                self.head = self.head.nextNode
                self.is_in_queue(data)
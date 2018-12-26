from binarysearchtree.Node import Node

class binar_search_tree(object):

    def __init__(self):
        self.root_Node = None

    def insert(self, data):
        if self.root_Node == None:
            self.root_Node = Node(data)
        else:
            self.root_Node.insert(data)

    def remove(self, data):
        if self.root_Node:
            if self.root_Node.data == data:
                temp_Node = Node(None)
                temp_Node.left_child = self.root_Node
                self.root_Node.remove(data, temp_Node)
            else:
                self.root_Node.remove(data, None)

    def getMax(self):
        if self.root_Node:
            return self.root_Node.getMax()

    def getMin(self):
        if self.root_Node:
            return self.root_Node.getMin()

    def traverse_orderly(self):
        if self.root_Node:
            self.root_Node.traverse_in_order()

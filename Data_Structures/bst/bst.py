from Data_Structures.bst.Node import Node as n

class bst(n):
    def __init__(self):
        self.count = 0
        self.root = None

    def insert(self, node):
        if self.root

    def del_node(self, data):
        pass

    def traverse(self):
        self.print_node(self.root)

    def print_node(self, node):
        # if node is not None
        if node != None:
        # print node.data
            print(node.data)
        # call print on right child
        self.print_node(node.right_child)
        # call print on left child
        self.print_node(node.left_child)
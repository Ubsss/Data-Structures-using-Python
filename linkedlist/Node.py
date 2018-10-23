class Node(object):
    def __init__(self, data):
        self.data = data
        self.nextNode = None;

    def remove(self, data, preciouNode):
        if self.data == data:
            preciouNode.nextNode = self.nextNode
            del self.data;
            del self.nextNode
        else:
            if self.nextNode is not None:
                self.nextNode.remove(data, self)
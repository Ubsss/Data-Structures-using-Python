from Data_Structures.hashtables.Node import Node

class hash_table(object):
    def __init__(self):
        self.capacity = 50
        self.size = 0
        self.buckets = [None] * self.capacity

    def hash(self, key):
        hashsum = 0

        # Enumerate provide an automatic counter, idx
        for idx, c in enumerate(key):
            # ord returns an int rep of a string
            hashsum += (idx + len(key)) ** ord(c)
            hashsum = hashsum % self.capacity
        return hashsum

    def insert(self,key,value):
        self.size += 1
        index = self.hash(key)
        node = self.buckets[index]
        if node is None:
            self.buckets[index] = Node(key, value)
            return
        prev = node
        while node is not None:
            prev = node
            node = node.next
        prev.next = Node(key, value)

    def find(self, key):
        index = self.hash(key)
        node = self.buckets[index]
        while node is not None and node.key != key:
            node = node.next

        if node is None:
            return None
        else:
            return node.value

    def remove(self,key):
        index = self.hash(key)
        node = self.buckets[index]

        while node is not None and node.key != key:
            prev = node
            node = node.next
        if node is None:
            return None
        else:
            self.size -= 1
            result = node.value
            if prev is None:
                node = None
            else:
                prev.next = prev.next.next
            return result

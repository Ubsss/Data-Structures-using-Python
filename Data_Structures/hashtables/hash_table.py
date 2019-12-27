from Data_Structures.hashtables.Node import node

class hash_table(node):
    def __init__(self):
        self.capacity = 10
        self.count = 0
        self.buckets = [None]*self.capacity

    def hash(self, key):
        hash_sum = 0
        for char in range(len(key)):
            hash_sum += ord(key[char])
        hash_sum %= self.capacity
        return hash_sum

    def insert(self, key, value):
        new_node = node(key,value)
        idx = self.hash(key)

        if self.buckets[idx] == None:
            self.buckets[idx] = new_node
            self.count += 1
            return True

        new_node.next = self.buckets[idx]
        self.buckets[idx] = new_node
        self.count +=1
        return True

    def find(self, key):
        idx = self.hash(key)

        pointer = node(None,None)
        pointer.next = self.buckets[idx]

        while pointer.next != None:
            if pointer.next.key == key:
                return True
            pointer.next = pointer.next.next

        del pointer
        return False

    def delete(self, key):
        idx = self.hash(key)

        pointer = self.buckets[idx]
        prev = None

        while pointer != None and pointer.key != key:
            prev = pointer
            pointer = pointer.next

        if pointer == None:
            return False
        else:
            if prev == None:
                self.buckets[idx] = pointer.next
            else:
                prev.next = pointer.next
                del pointer

            self.count -= 1
            return True

    def print(self):
        print("The HashTable contains " + str(self.count)+ " items: ")
        pointer = node(None, None)
        for i in range(self.capacity):
            pointer.next = self.buckets[i]
            while pointer.next != None:
                print(str(i) + " -> " + str(pointer.next.key) + " , " + str(pointer.next.value))
                pointer.next = pointer.next.next
        del pointer
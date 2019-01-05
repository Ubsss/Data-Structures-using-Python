from Data_Structures.doublylinkedlist.Node import node

class doubly_linked_list(node):
    def __init__(self):
        self.count = 0
        self.head = node(None)

    def insert(self, data):
        new_node = node(data)

        if self.head.next == None:
            self.head.next = new_node
            new_node.prev = self.head
            self.count += 1
            return True

        new_node.next = self.head.next
        new_node.prev = self.head
        new_node.next.prev = new_node
        self.head.next = new_node
        self.count += 1
        return True

    def del_item(self, item):
        pointer = node(None)

        if self.head.next == None:
            return False

        pointer.next =self.head.next

        while pointer.next != None:
            if pointer.next.data == item:
                if pointer.next.next == None:
                    pointer.next.prev.next = pointer.next.next
                    del pointer.next
                    del pointer
                    return True
                pointer.next.prev.next = pointer.next.next
                pointer.next.next.prev = pointer.next.prev
                del pointer.next
                del pointer
                return True
            else:
                pointer.next = pointer.next.next
        return False

    def find_item(self, item):
        pointer = node(None)

        if self.head.next == None:
            return False
        else:
            pointer.next = self.head.next
            while pointer.next != None:
                if pointer.next.data == item:
                    return True
                pointer.next = pointer.next.next

        del pointer
        return False

    def print_list(self):
        temp = node(None)

        if self.head.next != None:
            temp.next = self.head.next
        else:
            return "List is empty"
        while temp.next != None:
            print(temp.next.data)
            temp.next = temp.next.next
        del temp
        return True
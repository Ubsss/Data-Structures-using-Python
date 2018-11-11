class Heap(object):

    heap_size = 10

    def __init__(self):
        self.heap = [0]*Heap.heap_size
        self.current_postition = -1

    def insert(self, item):

        if self.is_full():
            print("Heap is full")
            return

        self.current_postition = self.current_postition + 1
        self.heap[self.current_postition] = item
        self.fix_up(self.current_postition)

    def is_full(self):
        if self.current_postition == Heap.heap_size:
            return True
        else:
            return False

    def fix_up(self, index):
        parent_index = int((index-1)/2)

        while parent_index >= 0 and self.heap[parent_index] < self.heap[index]:
            temp = self.heap[index]
            self.heap[index] = self.heap[parent_index]
            self.heap[parent_index] = temp
            parent_index = int((index-1)/2)

    def get_max(self):
        result = self.heap[0]
        self.current_postition = self.current_postition - 1
        self.heap[0] = self.heap[self.current_postition]
        del self.heap[self.current_postition+1]
        self.fix_down(0,-1)
        return result

    def fix_down(self, index, upto):
        if upto < 0:
            upto = self.current_postition

        while index <= upto:
            left_child = 2*index+1
            right_child = 2*index+2

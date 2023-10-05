class Heap:
    def __init__(self):
        self.heap = []

    def _heapup(self, index):
        parent_index = (index - 1) // 2
        while index > 0 and self.heap[index] < self.heap[parent_index]:
            # Swap the elements
            temp = self.heap[index]
            self.heap[index] = self.heap[parent_index]
            self.heap[parent_index] = temp

            index = parent_index
            parent_index = (index - 1) // 2


    def push(self, value):
        self.heap.append(value)
        self._heapup(len(self.heap) - 1)



    def print(self):
        print("This is my Heap:", self.heap)

heap = Heap()
heap.push(4)
heap.push(1)
heap.print()

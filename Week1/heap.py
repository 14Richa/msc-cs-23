# (C) Program your solution by completing the code below

class MinHeap:
    def __init__(self):
        self.H = [None]

    def size(self):
        return len(self.H)-1

    def __repr__(self):
        return str(self.H[1:])

    def satisfies_assertions(self):
        for i in range(2, len(self.H)):
            assert self.H[i] >= self.H[i //
                                       2],  f'Min heap property fails at position {i//2}, parent elt: {self.H[i//2]}, child elt: {self.H[i]}'

    def min_element(self):
        return self.H[1]

    # bubble_up function at index
    def bubble_up(self, index):
        assert index >= 1
        if index == 1:
            return

        parent = index // 2
        if self.H[index] < self.H[parent]:
            self.H[index], self.H[parent] = self.H[parent], self.H[index]
            self.bubble_up(parent)

    # bubble_down function at index
    def bubble_down(self, index):
        assert index >= 1 and index < len(self.H)
        lchild_index = 2 * index
        rchild_index = 2 * index + 1
        # code up your algorithm here
        # your code here
        smallest_index = index
        if lchild_index < len(self.H) and self.H[lchild_index] < self.H[smallest_index]:
            smallest_index = lchild_index
        if rchild_index < len(self.H) and self.H[rchild_index] < self.H[smallest_index]:
            smallest_index = rchild_index

        # If the smallest child is not the current node, swap them and continue bubbling down
        if smallest_index != index:
            self.H[index], self.H[smallest_index] = self.H[smallest_index], self.H[index]
            self.bubble_down(smallest_index)

    # Function: heap_insert
    # Insert elt into heap
    # Use bubble_up/bubble_down function

    def insert(self, elt):
        # your code here
        self.H.append(elt)
        index = len(self.H) - 1
        self.bubble_up(index)

    # Function: heap_delete_min
    # delete the smallest element in the heap. Use bubble_up/bubble_down
    def delete_min(self):
        # your code here
        self.H[1] = self.H[-1]
        self.H.pop()  # remove the last element

        # Start bubbling down from the root to maintain the min-heap property
        self.bubble_down(1)


my_heap = MinHeap()
# Insert elements into the heap
my_heap.insert(10)
my_heap.insert(5)
my_heap.insert(20)


minimum_element = my_heap.min_element()
print("Minimum element:", minimum_element)

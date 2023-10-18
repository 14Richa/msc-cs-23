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
        
        # your code here
        parent = index // 2
        if len(self.H) == 2:
            return
        
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

        # if only 1 element left 
        if len(self.H) == 2:
            return
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
        assert len(self.H) > 1, "Cannot delete from empty heap"
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


class TopKHeap:
    
    # The constructor of the class to initialize an empty data structure
    def __init__(self, k):
        self.k = k
        self.A = []
        self.H = MinHeap()
        
    def size(self): 
        return len(self.A) + (self.H.size())
    
    def get_jth_element(self, j):
        assert 0 <= j < self.k-1
        assert j < self.size()
        return self.A[j]
    
    def satisfies_assertions(self):
        # is self.A sorted
        for i in range(len(self.A) -1 ):
            assert self.A[i] <= self.A[i+1], f'Array A fails to be sorted at position {i}, {self.A[i], self.A[i+1]}'
        # is self.H a heap (check min-heap property)
        self.H.satisfies_assertions()
        # is every element of self.A less than or equal to each element of self.H
        for i in range(len(self.A)):
            assert self.A[i] <= self.H.min_element(), f'Array element A[{i}] = {self.A[i]} is larger than min heap element {self.H.min_element()}'
        
    # Function : insert_into_A
    # This is a helper function that inserts an element `elt` into `self.A`.
    # whenever size is < k,
    #       append elt to the end of the array A
    # Move the element that you just added at the very end of 
    # array A out into its proper place so that the array A is sorted.
    # return the "displaced last element" jHat (None if no element was displaced)
    def insert_into_A(self, elt):
        print("k = ", self.k)
        assert(self.size() < self.k)
        self.A.append(elt)
        # code up your algorithm
        # your code here
        index = len(self.A) - 1
        while index > 0 and self.A[index] < self.A[index-1]: 
          self.A[index], self.A[index-1] = self.A[index-1], self.A[index]
          index -= 1

        return self.A[-1]
    
            
    # Function: insert -- insert an element into the data structure.
    # Code to handle when self.size < self.k is already provided
    def insert(self, elt):
        size = self.size()
        # If we have fewer than k elements, handle that in a special manner
        if size <= self.k:
            self.insert_into_A(elt)
            return 
        # Code up your algorithm here.
        # your code here

        if elt > self.H.min_element():
            temp = self.H.delete_min()
            self.insert_into_A(elt)
            self.H.insert(temp)
        else:
            self.H.insert(elt)

        if self.A[-1] < self.A[-2]:
            self.A[-1], self.A[-2] = self.A[-2], self.A[-1]
            index = len(self.A) - 2
            while index > 0 and self.A[index] < self.A[index - 1]:
                self.A[index], self.A[index - 1] = self.A[index - 1], self.A[index]
                index -= 1

        
    # Function: Delete top k -- delete an element from the array A
    # In particular delete the j^{th} element where j = 0 means the least element.
    # j must be in range 0 to self.k-1
    def delete_top_k(self, j):
        k = self.k
        assert self.size() > k # we need not handle the case when size is less than or equal to k
        assert j >= 0
        assert j < self.k

        # your code here
        # Delete element at index j
        temp = self.A[j]
        self.A[j] = self.A[-1]
        self.A.pop()

        # Bubble down to maintain sorted order
        index = j
        while index < len(self.A) - 1 and self.A[index] > self.A[index + 1]:
            self.A[index], self.A[index + 1] = self.A[index + 1], self.A[index]
            index += 1
        
        self.H.insert(temp)
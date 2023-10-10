##### (A) Design Insertion Algorithm

Suppose we wish to insert a new element with key j into this data structure. Describe the pseudocode. Your pseudocode must deal with two cases: when the inserted element j would be one of the least k elements i.e, it belongs to the array A; or when the inserted element belongs to the heap H.  How would you distinguish between the two cases?

You can assume that heap operations such as insert(H, key) and delete(H, index) are defined. Assume that the heap is indexed as H[1],...,H[n -k] with H[0] being unused. Assume n>k,  i.e, there are already more than k elements in the data structure.

What is the complexity of the insertion operation in the worst case in terms of k,n.

##### Solution

- **Case 1 : Element 'j' belongs to 'A':**

In this case, I'm dealing with the k smallest elements, which are stored in 'A'. I first check if there's space in 'A' for 'j'. If the number of elements in 'A' is less than 'k', it means there's space. So, I simply add 'j' to 'A'. However, to keep 'A' sorted, I sort it after adding 'j'.

- **Case 2 : Element 'j' belongs to 'H':**

If 'j' is larger than the kth largest element in 'A', it means 'j' doesn't belong to 'A', and we insert it into the min-heap 'H' and then run a function(heapify) to maintain the heap property.

Below is the pseudocode:

```
Insert_element(j):
    # check if there's space in A for j.
    if the number of elements in A is less than k:
        # insert j into A.
        A.append(j)
        # sort A.
        Sort(A)
    else:
        # insert j into the min-heap H.
        Insert(H, j)
        # check if heap property is unchanged by calling heapify function 
        heapify(H)

heapify(H):
      i = len(H) // 2
      while i >= 1:
        left_child = 2 * i
        right_child = 2 * i + 1
        smallest = i
        # compare the current element to its children.
        if left_child < len(H) and H[left_child] < H[smallest]:
          smallest = left_child
        if right_child < len(H) and H[right_child] < H[smallest]:
          smallest = right_chil 
        # If the current node is not the smallest, change it with the smallest child.
        if smallest != i:
          change H[i] and H[smallest]
          heapify(H, smallest)

```

> The worst-case time complexities are:

- If 'j' belongs to 'A': O(k)
- If 'j' belongs to 'H': O(log(n))



##### (B) Design Deletion Algorithm

Suppose we wish to delete an index j from the top-k array A. Design an algorithm to perform this deletion. Assume that the heap is not empty, in which case you can assume that the deletion fails.

You can assume that heap operations such as insert(H, key) and delete(H, index) are defined. Assume that the heap is indexed as H[1],...,H[n -k] with H[0] being unused. Assume n>k, i.e, there are already more than k elements in the data structure.

What is the complexity of the deletion operation in the worst case in terms of k,n.

##### Solution 

The `delete(j)` function removes the element at index j from the top-k array. It first checks if the index j is within the range of the array A. If it is, then the element at index j is swapped with the last element in A and then removed from the array. Otherwise, the element at index j is removed from the min-heap H.

If the largest element in A is greater than the smallest element in H, then the two elements are swapped and then the `heapify(H)` function restores the heap property of the min-heap H

Below is the pseudocode:

```
delete(j):
    if 0 <= j < k:
        # swap the element at index j with the last element in A.
        swap A[j] and A[-1]
        # remove the last element from A.
        A.pop()
    else:
        # remove the element at index j from the H.
        delete(H, j)
        # if the largest element in A is greater than the smallest element in H, change them.
        if A[k - 1] > H[1]:
          swap A[k - 1] and H[1]
          heapify(H)

heapify(H):
      i = len(H) // 2
      while i >= 1:
        left_child = 2 * i
        right_child = 2 * i + 1
        smallest = i
        # compare the current element to its children.
        if left_child < len(H) and H[left_child] < H[smallest]:
          smallest = left_child
        if right_child < len(H) and H[right_child] < H[smallest]:
          smallest = right_child
        # If the current node is not the smallest, change it with the smallest child.
        if smallest != i:
          swap H[i] and H[smallest]
          heapify(H, smallest)
```

> The worst-case time complexity of the deletion operation is O(log k).
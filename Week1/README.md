##### (A) Design Insertion Algorithm

Suppose we wish to insert a new element with key j into this data structure. Describe the pseudocode. Your pseudocode must deal with two cases: when the inserted element j would be one of the least k elements i.e, it belongs to the array A; or when the inserted element belongs to the heap H.  How would you distinguish between the two cases?

You can assume that heap operations such as insert(H, key) and delete(H, index) are defined. Assume that the heap is indexed as H[1],...,H[n -k] with H[0] being unused. Assume n>k,  i.e, there are already more than k elements in the data structure.

What is the complexity of the insertion operation in the worst case in terms of k,n.

##### Solution

- Case 1 : Element 'j' belongs to 'A':

In this case, I'm dealing with the k smallest elements, which are stored in 'A'. I first check if there's space in 'A' for 'j'. If the number of elements in 'A' is less than 'k', it means there's space. So, I simply add 'j' to 'A'. However, to keep 'A' sorted, I sort it after adding 'j'.

- Case 2 : Element 'j' belongs to 'H':

If 'A' is already full, I need to decide whether 'j' belongs to 'A' or 'H'. To do this, I compare 'j' with the largest element in 'A'. If 'j' is smaller than the largest element in 'A', it means 'j' should be part of 'A'. In this case, I will remove the largest element from 'A', add 'j' to 'A', and sort 'A'.

If 'j' is larger than the kth largest element in 'A', it means 'j' doesn't belong to 'A', and we insert it into the min-heap 'H'.
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
        # compare j with the largest element in A.
        if j <= A[k - 1]:
            # j belongs to A because it's smaller to the largest element in A.
            # remove the largest element from A.
            A.pop()
            # Insert j into A.
            A.append(j)
            # sort A
            Sort(A)
        else:
            # j belongs to H as it's larger than the kth smallest element in A.
            # insert j into the min-heap H.
            Insert(H, j)
```

> The worst-case time complexities are:

- If 'j' belongs to 'A': O(k)
- If 'j' belongs to 'H': O(log(n))



##### (B) Design Deletion Algorithm

Suppose we wish to delete an index j from the top-k array A. Design an algorithm to perform this deletion. Assume that the heap is not empty, in which case you can assume that the deletion fails.

You can assume that heap operations such as insert(H, key) and delete(H, index) are defined. Assume that the heap is indexed as H[1],...,H[n -k] with H[0] being unused. Assume n>k, i.e, there are already more than k elements in the data structure.

What is the complexity of the deletion operation in the worst case in terms of k,n.

##### Solution 

If 'j' is in 'A' I will remove the element at index 'j' from 'A.' and to fill the gap left by the removed element, by taking the smallest element from 'H' and put it into 'A' and sort A.


```
DeleteFromA(j):
    if 0 <= j < k:
        # remove the element at index 'j' from 'A.'
        A.pop(j)
        # get the smallest element from 'H.'
        smallest_from_H = H[1]  # The root of the min-heap 'H' is the smallest element.
        # remove the smallest element from 'H'.
        Delete(H, 1)
        # insert the smallest element from 'H' into 'A' at index 'j.'
        A.insert(j, smallest_from_H)
        # sort A
        Sort(A)
```

> The worst-case time complexity of the deletion operation is O(k * log(k)).
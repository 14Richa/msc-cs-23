import random
# Week 3 - In class activity

class Node: 
    # Implement a node of the binary search tree.
    # Constructor for a node with key and a given parent
    # parent can be None for a root node.
    def __init__(self, key, parent = None): 
        self.key = key
        self.parent = parent 
        self.left = None # We will set left and right child to None
        self.right = None
        # Make sure that the parent's left/right pointer
        # will point to the newly created node.
        if parent != None:
            if key < parent.key:
                assert(parent.left == None), 'parent already has a left child -- unable to create node'
                parent.left = self
            else: 
                assert key > parent.key, 'key is same as parent.key. We do not allow duplicate keys in a BST since it breaks some of the algorithms.'
                assert(parent.right == None ), 'parent already has a right child -- unable to create node'
                parent.right = self
        
    # Utility function that keeps traversing left until it finds 
    # the leftmost descendant
    def get_leftmost_descendant(self):
        if self.left != None:
            return self.left.get_leftmost_descendant()
        else:
            return self
    
    # TODO: Complete the search algorithm below
    # You can call search recursively on left or right child
    # as appropriate.
    # If search succeeds: return a tuple True and the node in the tree
    # with the key we are searching for.
    # Also note that if the search fails to find the key 
    # you should return a tuple False and the node which would
    # be the parent if we were to insert the key subsequently.
    def search(self, key):
        if self.key == key: 
            return (True, self)
        # your code here
        if key < self.key:
            if self.left:
              return self.left.search(key)
            else:
              return (False, self)

        if key > self.key:
            if self.right:
              return self.right.search(key)
            else:
              return (False, self)
    
    #TODO: Complete the insert algorithm below
    # To insert first search for it and find out
    # the parent whose child the currently inserted key will be.
    # Create a new node with that key and insert.
    # return None if key already exists in the tree.
    # return the new node corresponding to the inserted key otherwise.
    def insert(self, key):
        # your code here
        found, parent = self.search(key)
        if found:
            return None        
        new_node = Node(key, parent)
        if key < parent.key:
            parent.left = new_node
        else:
            parent.right = new_node        
        return new_node
    
    # TODO: Complete algorithm to compute height of the tree
    # height of a node whose children are both None is defined
    # to be 1.
    # height of any other node is 1 + maximum of the height 
    # of its children.
    # Return a number that is the height.
    def height(self):
        # your code here
        if self.left is None and self.right is None:
            return 1
        left_height = 0
        if self.left:
            left_height = self.left.height()
        right_height = 0  
        if self.right:
            right_height = self.right.height()
        return 1 + max(left_height, right_height)
    
    #TODO: Write an algorithm to delete a key in the tree.
    # First, find the node in the tree with the key.
    # Recommend drawing pictures to visualize these cases below before
    # programming.
    # Case 1: both children of the node are None
    #   -- in this case, deletion is easy: simply find out if the node with key is its
    #      parent's left/right child and set the corr. child to None in the parent node.
    # Case 2: one of the child is None and the other is not.
    #   -- replace the node with its only child. In other words,
    #      modify the parent of the child to be the to be deleted node's parent.
    #      also change the parent's left/right child appropriately.
    # Case 3: both children of the parent are not None.
    #    -- first find its successor (go one step right and all the way to the left).
    #    -- function get_leftmost_descendant may be helpful here.
    #    -- replace the key of the node by its successor.
    #    -- delete the successor node.
    # return: no return value specified
    
    def delete(self, key):
        (found, node_to_delete) = self.search(key)
        assert(found == True), f"key to be deleted:{key}- does not exist in the tree"
        # your code here
        # Case 1: both children of the node are None
        if node_to_delete.left is None and node_to_delete.right is None:
            if node_to_delete.parent is not None:
                if node_to_delete == node_to_delete.parent.left:
                    node_to_delete.parent.left = None
                else:
                    node_to_delete.parent.right = None
            del node_to_delete
        # Case 2: one of the child is None and the other is not.
        elif node_to_delete.left is None or node_to_delete.right is None:
            child = node_to_delete.left if node_to_delete.left else node_to_delete.right
            if node_to_delete.parent is not None:
                if node_to_delete == node_to_delete.parent.left:
                    node_to_delete.parent.left = child
                else:
                    node_to_delete.parent.right = child
                child.parent = node_to_delete.parent
            else:
                node_to_delete.key = child.key
                node_to_delete.left = None
                node_to_delete.right = None
        # Case 3: both children of the parent are not None.
        else:
            successor = node_to_delete.right.get_leftmost_descendant()
            node_to_delete.key = successor.key
 
            if successor.parent.left == successor:
                successor.parent.left = None
            else:
                successor.parent.right = None
            del successor

# Week 3 - Task

# 1. make list of  numbers from 0 to n-1
# 2. randomly shuffle the list
# 3. insert the random list elements in order into a tree.
# 4. return the height of the resulting ree.
def run_single_experiment(n):
    # your code here
    # list of numbers from 0 to n-1
    numbers = list(range(n))
    # randomly shuffle the list
    random.shuffle(numbers)
    # insert the random list elements in order into a tree.
    root = Node(numbers[0])
    for i in range(1, len(numbers)):
        root.insert(numbers[i])
    # height of the resulting ree.
    return root.height()
   
def run_multiple_trials(n, numTrials):
    lst_of_depths = [run_single_experiment(n) for j in range(numTrials)]
    return (sum(lst_of_depths)/len(lst_of_depths), lst_of_depths)
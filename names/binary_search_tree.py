import sys
sys.path.append('../queue_and_stack')
from dll_queue import Queue
from dll_stack import Stack


class BinarySearchTree:
    def __init__(self, value):
        self.value = value #root
        self.left = None
        self.right = None
        self.stack = Stack()
        self.queue = Queue()

    # Insert the given value into the tree
    def insert(self, value):
        # pass
        if value < self.value:
            if self.left is None:
                self.left = BinarySearchTree(value)
            else:
                self.left.insert(value)
        else:
            if self.right is None:
                self.right = BinarySearchTree(value)
            else:
                self.right.insert(value)



    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        # pass
        if  self.value == target:
            return True
        
        if self.left is None and self.right is None:
            return False
        
        if target < self.value and self.left is not None:
            return self.left.contains(target)
        elif self.right is not None:
            return self.right.contains(target)



    # Return the maximum value found in the tree
    def get_max(self):
        # pass
        if self.value is None:
            return None
        
        if self.right is None:
            return self.value
        else:
            return self.right.get_max()

    # Call the function `cb` on the value of each node
    # You may use a recursive or iterative approach
    def for_each(self, cb):
        # pass
        if self.value is None:
            return None
        cb(self.value)
        if self.right is not None:
            self.right.for_each(cb)
        if self.left is not None:
            self.left.for_each(cb)
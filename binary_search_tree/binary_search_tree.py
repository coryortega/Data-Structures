import sys
sys.path.append('../queue_and_stack')
from dll_queue import Queue
from dll_stack import Stack


class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        # check if empty
            # if empty, put node here/atroot
        if self is None:
            self = value
        # otherwise
        else:
            # if new is LESS than node.value, go LEFT
            if value < self.value:
                if self.left is None:
                    self.left = BinarySearchTree(value)
                    return
                else:
                    self.left.insert(value)
            # if new value is GREATER than or EQUAL to node.value, go RIGHT
            else:
                if self.right is None:
                    self.right = BinarySearchTree(value)
                    return
                else:
                    self.right.insert(value)
        

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        # if node.value == findvalue
            # return true
        # else
            # if find < node.value
                # if node.left
                    # find on left node
                # else
                    # if node.right
                        # find on riight node
        pass

    # Return the maximum value found in the tree
    def get_max(self):
        # if theres no value to the right
        if self.right is None:
            # then return the root value
            return self.value
        # else, if there IS a value to the right
        else:
            current = self
            if current:
                while current.right is not None:
                    print(current.value)
                    current = current.right
                return current.value
            # return node.value
        pass

    # Call the function `cb` on the value of each node
    # You may use a recursive or iterative approach
    def for_each(self, cb):
        pass

    # DAY 2 Project -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        pass

    # STRETCH Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self, node):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        pass

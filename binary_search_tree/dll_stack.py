import sys
sys.path.append('../doubly_linked_list')
from doubly_linked_list import DoublyLinkedList

class Stack:
    def __init__(self):
        self.size = 0
        self.storage = DoublyLinkedList()
        # Why is our DLL a good choice to store our elements?
        # self.storage = ?

    def push(self, value):
        # add one to our size attribute to keep track of length
        self.size += 1
        # add to head of list, as if we're stacking
        self.storage.add_to_head(value)

    def pop(self):
        # if size is 0, then there's nothing to pop so just return
        if self.size == 0:
            return
        # if size is greater than 0, decrement the size by 1 and remove the value from the head
        self.size -= 1
        return self.storage.remove_from_head()

    def len(self):
        return self.size
        

import sys
sys.path.append('../doubly_linked_list')
from doubly_linked_list import DoublyLinkedList


class Queue:
    def __init__(self):
        self.size = 0
        self.storage = DoublyLinkedList()
        # Why is our DLL a good choice to store our elements?
        # self.storage = ?

    def enqueue(self, value):
        # adding value to the beginning, or tail, of the list
        self.storage.add_to_tail(value)
        # incrementing size by 1 to keep track of the size
        self.size += 1
        return

    def dequeue(self):
        # if size is 0, then theres nothing to deque
        if self.size == 0:
            return
        # if the size is greater than 0, then decrement the size attribute and remove from front of list
        self.size -= 1
        return self.storage.remove_from_head()

    def len(self):
        return self.size

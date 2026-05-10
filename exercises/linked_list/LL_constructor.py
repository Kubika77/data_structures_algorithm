class Node:
    def __init__(self, value: int) -> None:
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self, value: int) -> None:
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1
    
    def append(self, value: int) -> None:
        pass

    def prepend(self, value: int) -> None:
        pass

    def insert(self, value: int, index: int) -> None:
        pass

my_linked_list = LinkedList(4)
print(my_linked_list.head.value)

import sys
print(f"sys.path: {sys.path}")
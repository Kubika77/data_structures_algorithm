class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1
    
    def get_list_values(self):
        dll_values_list = []
        tmp = self.head
        for _ in range(self.length):
            dll_values_list.append(tmp.value)
            tmp = tmp.next
        return dll_values_list
    
    def append_value(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        self.tail.next = new_node
        new_node.prev = self.tail
        self.tail = new_node
        self.length += 1
        return True


my_dll = DoublyLinkedList(1)
for value in [2, 3, 4, 5]:
    my_dll.append_value(value)
print(f"my dll values are: {my_dll.get_list_values()}")
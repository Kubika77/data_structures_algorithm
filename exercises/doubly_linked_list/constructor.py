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


my_dll = DoublyLinkedList(7)
print(f"my dll values are: {my_dll.get_list_values()}")
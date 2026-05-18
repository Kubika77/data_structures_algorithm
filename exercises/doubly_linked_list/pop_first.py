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
    
    def pop_node(self):
        if self.length == 0:
            return None
        tmp = self.tail
        if self.length == 1:
            self.tail = None
            self.head = None
        else:
            self.tail = self.tail.prev
            self.tail.next = None
        tmp.prev = None
        self.length -= 1
        return tmp

    def prepend_node(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        self.length += 1
        return True
    
    def pop_first(self):
        if self.length == 0:
            return None
        tmp = self.head
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
            self.head.prev = None
        tmp.next = None
        self.length -= 1
        return tmp



my_dll = DoublyLinkedList(1)
for value in [2, 3, 4, 5]:
    my_dll.append_value(value)
print(f"my dll before poped first is:\n{my_dll.get_list_values()}")
for _ in range(my_dll.length):
    poped = my_dll.pop_first()
    print(f"poped value is: {poped.value}, and new list is: {my_dll.get_list_values()}")

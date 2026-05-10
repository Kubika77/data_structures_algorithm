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

    def get_list(self):
        dl_list = []
        tmp = self.head
        for _ in range(self.length):
            dl_list.append(tmp.value)
            tmp = tmp.next
        return dl_list

    def append_node(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        self.tail.next = new_node
        new_node.prev = self.tail
        self.tail = new_node
        self.length += 1
        return True
    
    def get_node(self, index):
        if index < 0 or index >= self.length:
            return None
        if index < self.length/2:
            temp = self.head
            for _ in range(index):
                temp = temp.next
        else:
            temp = self.tail
            for _ in range(self.length - 1, index, -1):
                temp = temp.prev
        return temp


my_dll = DoublyLinkedList(1)
for value in [2, 3, 4, 5]:
    my_dll.append_node(value)
print(f"my dll list is: {my_dll.get_list()}")
print(f"the 2nd node value in list is: {my_dll.get_node(0).value}")
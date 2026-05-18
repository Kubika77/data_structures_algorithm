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
    
    # This is for set node without using the get_node:
    #
    # def set_node(self, index, value):
    #     if index < 0 or index >= self.length:
    #         return None
    #     if index < self.length/2:
    #         tmp = self.head
    #         for _ in range(index):
    #             tmp = tmp.next
    #     else:
    #         tmp = self.tail
    #         for _ in range(self.length -1, index, -1):
    #             tmp = tmp.prev
    #     tmp.value = value
    #     return True
    
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
    
    def set_node(self, index, value):
        tmp = self.get_node(index)
        if tmp:
            tmp.value = value
            return True
        return False

my_dll = DoublyLinkedList(1)
for value in [2, 3, 4, 5]:
    my_dll.append_node(value)
print(f"my dll list before set is: {my_dll.get_list()}")
my_dll.set_node(4, 12)
print(f"my dll list after set index 4 to 12 is: {my_dll.get_list()}")
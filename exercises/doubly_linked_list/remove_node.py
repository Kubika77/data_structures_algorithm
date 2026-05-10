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
    
    def insert_node(self, index, value):
        if index < 0 or index > self.length:
            return None
        if index == 0:
            self.prepend_node(value)
        elif index == self.length:
            self.append_node(value)
        else:
            new_node = Node(value)
            before = self.get_node(index -1)
            after = before.next
            before.next = new_node
            new_node.prev = before
            new_node.next = after
            after.prev = new_node
            self.length += 1
        return True
    
    def remove_node(self, index):
        print(f"length is: {self.length}")
        if index < 0 or index > self.length:
            return None
        if index == 0:
            self.pop_first()
        elif index == self.length - 1:
            self.pop_node()
        else:
            # another way to do it but less readable:
            #
            # tmp = self.get_node(index)
            # tmp.prev.next = tmp.next
            # tmp.next.prev = tmp.prev
            before = self.get_node(index - 1)
            tmp = before.next
            after = tmp.next
            before.next = after
            after.prev = before
            tmp.prev = None
            tmp.next = None
            self.length -= 1
            return tmp



my_dll = DoublyLinkedList(1)
for value in [2, 3, 4, 5]:
    my_dll.append_node(value)
print(f"my dll list before insert node is: {my_dll.get_list()}")
my_dll.remove_node(4)
print(f"my dll list after set index 1 to 12 is: {my_dll.get_list()}")
                
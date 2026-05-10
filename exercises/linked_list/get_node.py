class Node:
    def __init__(self, value: int):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self, value: int):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def append(self, value: int) -> bool:
        new_node: Node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1
        return True

    def get(self, idx: int):
        if idx < 0 or idx >= self.length:
            return None
        tmp_node = self.head
        for _ in range(idx):
            tmp_node = tmp_node.next
        return tmp_node.value

ll = LinkedList(0)
for value in [1, 2, 3, 4, 5]:
    ll.append(value)
print (f"item index {0} in list is: {ll.get(0)}")
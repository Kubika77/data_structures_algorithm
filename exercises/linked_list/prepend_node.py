class Node:
    def __init__(self, value: int) -> None:
        self.value = value
        self.next: Node | None = None


class LinkedList:
    def __init__(self, value: int) -> None:
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1
    
    def get_list(self) -> list[int]:
        temp: Node | None = self.head
        linked_list_values = []
        while temp is not None:
            linked_list_values.append(temp.value)
            temp = temp.next
        return linked_list_values
    
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
    
    def pop(self) -> Node | None:
        temp: Node | None = self.head
        pre_temp: Node | None = self.head
        if self.length == 0:
            return None
        while temp.next is not None:
            pre_temp = temp
            temp = temp.next
        self.tail = pre_temp
        self.tail.next = None
        self.length -= 1
        if self.length == 0:
            self.head = None
            self.tail = None
        return temp

    def prepend(self, value: int) -> bool:
        new_node: Node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.length += 1
        return True
    
    def pop_first(self) -> Node | None:
        if self.length == 0:
            return None
        tmp: Node | None = self.head
        self.head = self.head.next
        tmp.next = None
        self.length -= 1
        if self.length == 0:
            self.tail = None
        return tmp
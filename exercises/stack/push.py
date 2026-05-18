class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Stack:
    def __init__(self, value):
        new_node = Node(value)
        self.top = new_node
        self.height = 1

    def get_stack(self):
        tmp = self.top
        stack_items = []
        while tmp is not None:
            stack_items.append(tmp.value)
            tmp = tmp.next
        return stack_items

    def push(self, value):  
        new_node = Node(value)
        if self.height == 0:
            self.top = new_node
        else:
            new_node.next = self.top
            self.top = new_node
        self.height += 1

my_stack = Stack(1)
my_stack.push(2)
my_stack.push(3)
print(f"my stack is: {my_stack.get_stack()}")
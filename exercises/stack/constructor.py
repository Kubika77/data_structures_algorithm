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

my_stack = Stack(4)
print(f"my stack is: {my_stack.get_stack()}")
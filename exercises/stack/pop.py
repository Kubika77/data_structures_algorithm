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
    
    def pop(self):
        if self.height == 0:
            return None
        tmp = self.top
        self.top = self.top.next
        tmp.next = None
        self.height -= 1
        if self.height == 0:
            self.top = None
        return tmp


my_stack = Stack(1)
my_stack.push(2)
my_stack.push(3)
print(f"my stack is: {my_stack.get_stack()}")
poped = my_stack.pop()
print(f"popped 3 value is: {poped.value}")
print(f"my stack is: {my_stack.get_stack()}")
poped = my_stack.pop()
print(f"popped 2 value is: {poped.value}")
print(f"my stack is: {my_stack.get_stack()}")
poped = my_stack.pop()
print(f"popped 1 value is: {poped.value}")
print(f"my stack is: {my_stack.get_stack()}")
poped = my_stack.pop()
print(f"popped None value is: {poped}")
print(f"my stack is: {my_stack.get_stack()}")
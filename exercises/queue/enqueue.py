class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class Queue:
    def __init__(self, value):
        new_node = Node(value)
        self.first = new_node
        self.last = new_node
        self.length = 1

    def get_queue(self):
        queue_entity = []
        tmp = self.first
        while tmp is not None:
            queue_entity.append(tmp.value)
            tmp = tmp.next
        return queue_entity
    
    def enqueue(self, value):
        new_node = Node(value)
        if self.first is None:
            self .first = new_node
            self.last = new_node
        else:
            self.last.next = new_node
            self.last = new_node
        self.length += 1


my_queue = Queue(1)
print(f"my queue is: {my_queue.first.value}, {my_queue.last.value}, length: {my_queue.length}")
print(f" my queue is: {my_queue.get_queue()}")
my_queue.enqueue(2)
print(f" my queue is: {my_queue.get_queue()}")
my_queue.enqueue(3)
print(f" my queue is: {my_queue.get_queue()}")
my_queue.enqueue(4)
print(f" my queue is: {my_queue.get_queue()}")
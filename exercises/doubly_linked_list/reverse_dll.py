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

    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next
        
    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        self.length += 1
        return True
        
    # # solution 1:
    # #
    def reverse(self):
        if not self.head or not self.head.next:
            return

        current = self.head
        temp = None

        while current:
            temp = current.prev
            current.prev = current.next
            current.next = temp
            current = current.prev

        tmp_head = self.head
        self.head = self.tail
        self.tail = tmp_head


    # #solution 2:
    # #
    # def reverse(self):
    #     temp = self.head
    #     while temp is not None:
    #         # swap the prev and next pointers of node points to
    #         # when doing the swap in 1 line like this, the interperter first
    #         # evaluates the right side of the equation, then doing the assignment
    #         # in oppose to doing it in 2 lines, then you will need a third tmp var 
    #         # to store the original value so it want be changed before doing the last assignment
    #         temp.prev, temp.next = temp.next, temp.prev
            
    #         # move to the next node
    #         temp = temp.prev
            
    #     # swap the head and tail pointers
    #     self.head, self.tail = self.tail, self.head



my_doubly_linked_list = DoublyLinkedList(1)
my_doubly_linked_list.append(2)
my_doubly_linked_list.append(3)
my_doubly_linked_list.append(4)
my_doubly_linked_list.append(5)


print('DLL before reverse():')
my_doubly_linked_list.print_list()


my_doubly_linked_list.reverse()


print('\nDLL after reverse():')
my_doubly_linked_list.print_list()



"""
    EXPECTED OUTPUT:
    ----------------
    DLL before reverse():
    1 <-> 2 <-> 3 <-> 4 <-> 5
    
    DLL after reverse():
    5 <-> 4 <-> 3 <-> 2 <-> 1

"""


"""
Description

The merge method takes in another LinkedList as an input and merges it with the current LinkedList.

The elements in both lists are assumed to be in ascending order.

Parameters

other_list (LinkedList): the other LinkedList to merge with the current list



Return Value

This method does not return a value, but it modifies the current LinkedList to contain the merged list.



Example:

l1 = LinkedList(1)
l1.append(3)
l1.append(5)
l1.append(7)
 
l2 = LinkedList(2)
l2.append(4)
l2.append(6)
l2.append(8)
 
l1.merge(l2)
 
# The current list (l1) now contains the merged list [1, 2, 3, 4, 5, 6, 7, 8]


Detailed Steps:

Initialize Helper Nodes:

Create a "dummy" node that acts as a starting point, and give it a value of 0.

Create another node called "current" and set it to point to this dummy node. 
We'll use "current" to keep track of where we are in the new merged list.

Merge Loop:

This loop will go through each node in both the list we're working on (self.head) 
and the list we're merging into it (other_head).

For each pair of nodes (one from each list), compare their values.

Take the node with the smaller value and attach it to the "current" node.

Move both the "current" node and the list head that had the smaller value to their respective next nodes.

Check for Remaining Nodes:

After the loop, it's possible that one list still has nodes while the other doesn't.

If that's the case, take the remaining nodes from the list that isn't empty and attach them to "current".

Update Head, Tail, and Length:

Once you're done with the merging, the "dummy" node will still be at the start. 
Update the head of the list to point to the node that comes immediately after this dummy node.

Also, make sure to update the tail node to be the last node in the new, merged list.

Finally, update the length of the list to account for the nodes from both original lists.
"""

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        

class LinkedList:
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
            self.tail = new_node
        self.length += 1

    def merge(self, other_list):
        dummy = Node(0)
        current = dummy
        other_head = other_list.head
        self_head = self.head
        while self_head is not None and other_head is not None:
            if self_head.value > other_head.value:
                current.next = other_head
                other_head = other_head.next
            elif self_head.value < other_head.value:
                current.next = self_head
                self_head = self_head.next
            else:
                current.next = self_head
                self_head = self.head.next
                other_head = other_head.next
            current = current.next
        if self_head is not None:
            current.next = self_head
        if other_head is not None:
            current.next = other_head
            self.tail = other_list.tail
        self.head = dummy.next
        self.length += other_list.length


# # Shorter and more efficient implementation of the merge method:
#     def merge(self, other_list):
#         other_head = other_list.head
#         dummy = Node(0)
#         current = dummy
 
#         while self.head is not None and other_head is not None:
#             if self.head.value < other_head.value:
#                 current.next = self.head
#                 self.head = self.head.next
#             else:
#                 current.next = other_head
#                 other_head = other_head.next
#             current = current.next
 
#         if self.head is not None:
#             current.next = self.head
#         else:
#             current.next = other_head
#             self.tail = other_list.tail
 
#         self.head = dummy.next
#         self.length += other_list.length


l1 = LinkedList(1)
l1.append(3)
l1.append(5)
l1.append(7)


l2 = LinkedList(2)
l2.append(4)
l2.append(6)
l2.append(8)

l1.merge(l2)

l1.print_list()
print(f"head now is {l1.head.value}")
print(f"tail now is {l1.tail.value}")
print(f"length now is {l1.length}")


"""
    EXPECTED OUTPUT:
    ----------------
    1 
    2 
    3 
    4 
    5 
    6 
    7
    8
    head now is 1
    tail now is 8
    length now is 8
"""



"""
This code defines a method called merge that can be used on a LinkedList object to merge it with 
another LinkedList object (other_list). The method follows the merge sort algorithm to combine the two lists.

Here's how it works:

The method starts by getting the head node of the other_list and creating a dummy node to hold the merged list.

A current node is created to keep track of the position in the merged list.

A while loop is used to compare the values of the first nodes in both lists. 
The smaller value is added to the current node, and the respective head node is moved to the next position.

Steps 3 is repeated until one of the lists is empty.

If the first list still has nodes left, they are added to the current node.

If the second list still has nodes left, they are added to the current node.

The head of the merged list is set to the next node after the dummy node, 
and the length of the list is updated.

Note that this method assumes that both LinkedList objects are already sorted in ascending order. 
If not, the merge method could produce an incorrectly sorted merged list.



Code with inline comments:

# Method to merge a linked list with another linked list
def merge(self, other_list):
    
    # Get the head node of the other linked list
    other_head = other_list.head
    
    # Create a dummy node to hold the merged list
    dummy = Node(0)
    
    # Set the current node to the dummy node
    current = dummy
 
    # Loop while both lists still have nodes
    while self.head is not None and other_head is not None:
        
        # Compare the values of the first nodes in each list
        if self.head.value < other_head.value:
            # If the value in the first list is smaller,
            # add it to the current node and move to the next node in the first list
            current.next = self.head
            self.head = self.head.next
        else:
            # Otherwise, add the value from the second list
            # and move to the next node in the second list
            current.next = other_head
            other_head = other_head.next
            
        # Move the current node to the next position
        current = current.next
 
    # If the first list still has nodes left, add them to the current node
    if self.head is not None:
        current.next = self.head
    else:
        # If the second list still has nodes left, add them to the current node
        current.next = other_head
        # Update the tail of the merged list to be the tail of the second list
        self.tail = other_list.tail
 
    # Set the head of the merged list to the next node after the dummy node
    self.head = dummy.next
    
    # Update the length of the merged list
    self.length += other_list.length
"""
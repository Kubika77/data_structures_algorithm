class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None
    
    def __r_contains(self, current_node, value):
        if current_node == None:
            return False
        if current_node.value > value:
            return self.__r_contains(current_node.left, value)
        if current_node.value < value:
            return self.__r_contains(current_node.right, value)
        if current_node.value == value:
            return True
        
    def __r_insert(self, current_node, new_node):
        if current_node is None:
            return new_node
        if current_node.value > new_node.value:
            current_node.left = self.__r_insert(current_node.left, new_node)
        if current_node.value < new_node.value:
            current_node.right = self.__r_insert(current_node.right, new_node)
        # returning the pointer of the current node to the node pointing to it
        return current_node
    
    def __r_delete(self, current_node, value):
        if current_node == None:
            return None
        if value < current_node.value:
            current_node.left = self.__r_delete(current_node.left, value)
        elif value > current_node.value:
            current_node.right = self.__r_delete(current_node.right, value)
        # when code reaches this "else" state, it means that we found the value in the current node,
        # which than we need to delete, but the node needs to be deleted can be in 4 different situations, which we must handle sperately:
        # 1. when we want to delete a "leaf" node (with no left and right)
        # 2. when the Node we need to delete (with the value asked), has a right node connected without a left node
        # 3. when the Node we need to delete, has a left node connected without a right node
        # 4. when the value we need to delete is on a node which has both left and right nodes connected (and they are not None)
        else:
            # a case where the deleted node is a leaf (no left and no right)
            if current_node.left == None and current_node.right == None:
                return None
            # a case where deleted node has a right node connected only
            # in this case we are return current node as the right node connected to the deleted node
            elif current_node.left == None:
                current_node = current_node.right
            # a case where deleted node has a left node connected only
            # in this case we are return current node as the left node connected to the deleted node
            # so instead of the deleted node, we bring up the pointer to the left node of the deleted node,
            # so the previous node (of the deleted) will now point this.
            elif current_node.right == None:
                current_node = current_node.left
            # this is the 4th case where deleted node has both left and right nodes connected
            # for this case we need an helper method to find the minimum value in a particular sub tree (min_value)
            # for finding the minimum we need to recursivly go left down the nodes, until we will hit the 
            # "None", which means end of sub tree, so last value before None will be the min value/node
            else:
                sub_tree_min = self.min_value(current_node.right)
                current_node.value = sub_tree_min
                current_node.right = self.__r_delete(current_node.right, sub_tree_min)
        return current_node 
    
    def min_value(self, current_node):
        while current_node.left is not None:
            current_node = current_node.left
        return current_node.value

    def r_contains(self, value):
        return self.__r_contains(self.root, value)

    def r_insert(self, value):
        new_node = Node(value)
        if self.root is None:
            self.root = new_node
        self.__r_insert(self.root, new_node)
    
    def r_delete(self, value):
        self.root = self.__r_delete(self.root, value)


my_tree = BinarySearchTree()
my_tree.r_insert(2)
my_tree.r_insert(1)
my_tree.r_insert(3)

"""
       2
      / \
     1   3
"""

print("root:", my_tree.root.value)
print("root.left =", my_tree.root.left.value)
print("root.right =", my_tree.root.right.value)


my_tree.r_delete(2)

"""
       3
      / \
     1   None
"""


print("\nroot:", my_tree.root.value)
print("root.left =", my_tree.root.left.value)
print("root.right =", my_tree.root.right)



"""
    EXPECTED OUTPUT:
    ----------------
	root: 2
	root.left = 1
	root.right = 3

	root: 3
	root.left = 1
	root.right = None

"""
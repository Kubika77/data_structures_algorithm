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
        

    def r_contains(self, value):
        return self.__r_contains(self.root, value)

    def r_insert(self, value):
        new_node = Node(value)
        if self.root is None:
            self.root = new_node
        self.__r_insert(self.root, new_node)


my_tree = BinarySearchTree()
output = my_tree.r_insert(47)
# my_tree.r_insert(47)
my_tree.r_insert(21)
my_tree.r_insert(76)
my_tree.r_insert(18)
my_tree.r_insert(27)
my_tree.r_insert(52)
# testing insert a duplicate value.
# BST does not allow/add a duplicate value
# So in this case the current_node.value is not bigger or smaller than new_node.value
# so it will reach line 29, and return back the current_node (the pointer for the existing one)
my_tree.r_insert(52)
my_tree.r_insert(82)

print(f"output of r insert is: {output}")

print('\nBST Contains 47:')
print(my_tree.r_contains(47))

print('BST Contains 21:')
print(my_tree.r_contains(21))

print('BST Contains 76:')
print(my_tree.r_contains(76))

print('BST Contains 18:')
print(my_tree.r_contains(18))

print('BST Contains 27:')
print(my_tree.r_contains(27))

print('BST Contains 52:')
print(my_tree.r_contains(52))

print('BST Contains 82:')
print(my_tree.r_contains(82))

print('\nBST Contains 17:')
print(my_tree.r_contains(17))


# # Expected Results:
# BST Contains 47:
# True
# BST Contains 21:
# True
# BST Contains 76:
# True
# BST Contains 18:
# True
# BST Contains 27:
# True
# BST Contains 52:
# True
# BST Contains 82:
# True

# BST Contains 17:
# False
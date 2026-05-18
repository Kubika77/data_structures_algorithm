class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None
    
    def insert(self, value):
        new_node = Node(value)
        if self.root == None:
            self.root = new_node
            return True
        temp = self.root
        while (True):
            if new_node.value == temp.value:
                return False
            if new_node.value < temp.value:
                if temp.left is None:
                    temp.left = new_node
                    return True
                temp = temp.left
            else:
                if temp.right is None:
                    temp.right = new_node
                    return True
                temp = temp.right

    def __r_contains(self, current_node, value):
        if current_node == None:
            return False
        if current_node.value > value:
            return self.__r_contains(current_node.left, value)
        if current_node.value < value:
            return self.__r_contains(current_node.right, value)
        if current_node.value == value:
            return True

    def r_contains(self, value):
        return self.__r_contains(self.root, value)


my_tree = BinarySearchTree()
my_tree.insert(47)
my_tree.insert(21)
my_tree.insert(76)
my_tree.insert(18)
my_tree.insert(27)
my_tree.insert(52)
my_tree.insert(82)

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
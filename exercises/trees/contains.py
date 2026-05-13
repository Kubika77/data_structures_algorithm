class Node:
    def __init__(self, value):
        self.value = value
        self.right = None
        self.left = None

class BinarySearchTree:
    def __init__(self):
        self.root = None
    
    def insert(self, value):
        new_node = Node(value)
        if self.root is None:
            self.root = new_node
            return True
        tmp = self.root
        while (True):
            if tmp.value == value:
                return False
            if tmp.value > value:
                if tmp.left is None:
                    tmp.left = new_node
                    return True
                tmp = tmp.left
            elif tmp.value < value:
                if tmp.right is None:
                    tmp.right = new_node
                    return True
                tmp = tmp.right
            else:
                return False
    
    def contains(self, value):
        # # this edge case lines actually are not needed because if root is None
        # # than tmp will be None too (tmp = self.root), so while loop will break
        # # and False will be returned
        # if self.root == None:
        #     return False
        tmp = self.root
        while tmp is not None:
            if value > tmp.value:
                tmp = tmp.right
            elif value < tmp.value:
                tmp = tmp.left
            else:
                return True
        return False


my_tree = BinarySearchTree()
my_tree.insert(47)
my_tree.insert(21)
my_tree.insert(76)
my_tree.insert(18)
my_tree.insert(27)
my_tree.insert(52)
my_tree.insert(82)

value = 82
print(f"my bst contains {value}: {my_tree.contains(value)}")
print(f"BST root is: {my_tree.root.value}")
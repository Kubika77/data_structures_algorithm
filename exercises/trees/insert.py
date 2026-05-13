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
            if new_node.value < tmp.value:
                if tmp.left is None:
                    tmp.left = new_node
                    return True
                tmp = tmp.left
            elif new_node.value > tmp.value:
                if tmp.right is None:
                    tmp.right = new_node
                    return True
                tmp = tmp.right
            else:
                return False


my_tree = BinarySearchTree()
my_tree.insert(47)
my_tree.insert(21)
my_tree.insert(76)
my_tree.insert(18)
my_tree.insert(27)
my_tree.insert(52)
my_tree.insert(82)
print(f"BST root is: {my_tree.root.value}")

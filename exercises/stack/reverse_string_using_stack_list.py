class Stack:
    def __init__(self):
        self.stack_list = []

    def print_stack(self):
        for i in range(len(self.stack_list)-1, -1, -1):
            print(self.stack_list[i])

    def is_empty(self):
        return len(self.stack_list) == 0

    def peek(self):
        if self.is_empty():
            return None
        else:
            return self.stack_list[-1]

    def size(self):
        return len(self.stack_list)

    def push(self, value):
        self.stack_list.append(value)

    def pop(self):
        if self.is_empty():
            return None
        else:
            return self.stack_list.pop()


# # Solution 2:
# # reverse a tring using a reversed list:
# #
# def reverse_string(word):
#     rev_word = word[::-1]
#     return rev_word

def reverse_string(word):
    str_stack = Stack()
    for char in word:
        str_stack.push(char)
    rev_str = ""
    while not str_stack.is_empty():
        rev_str += str_stack.pop()
    return rev_str

        
my_string = 'hello'

print ( reverse_string(my_string) )



"""
    EXPECTED OUTPUT:
    ----------------
    olleh

"""

def functhree():
    print("three")

def functwo():
    functhree()
    print("two")

def funcone():
    functwo()
    print("one")

funcone()


# although we first called funcone(), the print will be reversed.
# this is because the call stack is actually a stack which acts as LIFO,
# so last function entered to callstack (which is functhree), will be the first
# to be executed, and so on.

# Expected Output:
# three
# two
# one
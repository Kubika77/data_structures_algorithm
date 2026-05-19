"""
In this file we will break the full list again and again until we have lists of length 1, and then we will merge those lists together in a sorted way,
Using the merge function that we have defined in the merge_helper.py file.
The merge helper will start with 2 lists of 1 item (which are already sorted) and will merge them together in a sorted way, 
and then we will merge the resulting list with another list of 1 item, 
and so on until we have merged all the lists together.

The break lists into smaller lists will be done using recursion (because each recursive call will handle a smaller portion of the list, 
and will do the same operation of breaking into half, until we reach the base case of lists of length 1), 
and the merge function will be called on the way back up the recursive calls.
"""

def merge_sort(arr):
    """
    This function breaks the input list into smaller lists until we have lists of length 1, 
    and then merges those lists together in a sorted way using the merge function.
    This function uses recursion which breaks the list into smaller lists until we reach the base case of lists of length 1,
    and then merges those lists together in a sorted way using the merge function.
    """
    # This is the base case for returning from the recursion
    # when the array was splitted until it is an one item list
    if len(arr) == 1:
        return arr
    mid = len(arr) // 2
    # this is the recursive case for splitting the array on and on
    left_half = merge_sort(arr[:mid])
    right_half = merge_sort(arr[mid:])
    # This is for merging back 2 sorted lists after the break of the long array.
    return merge(left_half, right_half)


def merge(list1, list2):
    """
    Merge two sorted lists into a single sorted list.
    """
    combined = []
    i = 0
    j = 0
    while i < len(list1) and j < len(list2):
        if list1[i] < list2[j]:
            combined.append(list1[i])
            i += 1
        else:
            combined.append(list2[j])
            j += 1
    while i < len(list1):
        combined.append(list1[i])
        i += 1
    while j < len(list2):
        combined.append(list2[j])
        j += 1
    return combined

array = [9, 5, 1, 3, 8, 2, 4, 7, 6]
print(f"Sorted list is: {merge_sort(array)}")
print(f"Original list is: {array}")

# EXPECTED OUTPUT:
# Sorted list is: [1, 2, 3, 4, 5, 6, 7, 8, 9]
# Original list is: [9, 5, 1, 3, 8, 2, 4, 7, 6]
#
# As you can see the original list is not changed, but the merge sort created
# and returned a sorted list, this is why space complexity is O(n), and not O(1)
# such as with other sort methods.
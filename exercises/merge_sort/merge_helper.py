"""
This function will start when we have 2 sorted lists and we want to merge them together sorted into one sorted list. 
This is the helper function for merge sort.
"""

def merge(list1, list2):
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
    # When we are reaching to this point, it could be that one of the lists is not fully traversed
    # (this could happen when the lists are of different lengths, and we have already 
    # added all the elements of the other list to the combined list.), 
    # so we need to add the remaining elements to the combined list.
    # and as it is already sorted, we can just add the remaining elements without any comparison.
    while i < len(list1):
        combined.append(list1[i])
        i += 1
    while j < len(list2):
        combined.append(list2[j])
        j += 1
    return combined


# MERGE REQUIRES TWO SORTED LISTS:
print(merge([1,2,7,8], [3,4,5,6]))



"""
    EXPECTED OUTPUT:
    ----------------
    [1, 2, 3, 4, 5, 6, 7, 8]
 """
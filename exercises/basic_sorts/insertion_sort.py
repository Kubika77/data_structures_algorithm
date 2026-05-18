def insertion_sort(my_list):
    # in insertion sort we start at the second item in list, search for minumum value
    # up to the end of the list, and bring the minimum value to the second index (index 1),
    # and then we do it one after each other to the rest of the items in list
    for i in range(1, len(my_list)):
        temp = my_list[i]
        j = i -1
        while temp < my_list[j] and j > -1:
            my_list[j + 1] = my_list[j]
            my_list[j] = temp
            j -= 1
    return my_list

print(insertion_sort([4, 2, 6, 5, 1, 3]))


# Expected output:
# [1, 2, 3, 4, 5, 6]

# Big O is O(n*2) as it is a nested loop
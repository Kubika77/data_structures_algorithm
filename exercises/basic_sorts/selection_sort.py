def selection_sort(my_list):
    for i in range(len(my_list) - 1):
        # index of the item of the lowest value
        min_index = i
        for j in range (i + 1, len(my_list)):
            if my_list[j] < my_list[min_index]:
                min_index = j
        # We need to do the swap only in case that the starting index (i) is different
        # than the min_index found. if it is already the minimum value, swap is not needed
        if i != min_index:
            temp = my_list[i]
            my_list[i] = my_list[min_index]
            my_list[min_index] = temp
    return my_list


print(selection_sort([4, 2, 6, 5, 1, 3]))


# Expected output:
# [1, 2, 3, 4, 5, 6]

# Big O is O(n*2) as it is a nested loop

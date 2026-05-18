def bubble_sort(my_list):
    for i in range(len(my_list) - 1, 0, -1):
        # in this loop we are moving again and agin the max value to the end of the list
        for j in range(i):
            if my_list[j] > my_list[j + 1]:
                temp = my_list[j]
                my_list[j] = my_list[j + 1]
                my_list[j + 1] = temp
    return my_list


print(bubble_sort([4, 2, 6, 5, 1, 3]))


# Expected output:
# [1, 2, 3, 4, 5, 6]

# Big O is O(n*2) as it is a nested loop
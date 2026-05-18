import pytest

"""
finding an item in common between 2 lists.
for example:
list1 = [1, 3, 5]
list2 = [2, 4, 5]

the function will find the "5" which is common on both lists
"""

# list1 = [1, 3, 5]
# list2 = [2, 4, 6]

# # worst case implementation will be nested for loops.
# # which will cause a big O of O(n*2)
# def item_in_common(list1, list2):
#     for item1 in list1:
#         for item2 in list2:
#             if item1 == item2:
#                 return item1
#     return None

# More efficient way to do it, is with using dicts (hash tables).
# we will iterate once on first list and store all items as keys,
# than we will iterate through the second list and check if item in second list,
# exists within the dictionary keys.
# this will be O(2n) which is actually O(n) (we can remove the constants - 2),
# so it is better than the first implemanation on nested loops which is O(n*2)
def item_in_common(list1, list2):
    list1_dict = {}
    for item1 in list1:
        list1_dict[item1] = True
    for item2 in list2:
        if item2 in list1_dict:
            return item2
    return None
    


@pytest.mark.parametrize("list_1, list_2, expected_common", [
    ([1, 3, 5], [2, 4, 5], 5),
    ([2], [2], 2),
    ([1, 2, 3], [4, 5, 6], None),
    (["a", "b", "c"], ["d", "e", "c"], "c"),
])
def test_item_in_common(list_1, list_2, expected_common):
    assert expected_common == item_in_common(list_1, list_2)


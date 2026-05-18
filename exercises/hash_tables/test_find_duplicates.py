import pytest


# # basic without copunting the number of times item found in list
# def find_duplicates(array):
#     duplicates = []
#     nums_dict = {}
#     for item in array:
#         if item not in nums_dict:
#             nums_dict[item] = True
#         else:
#             if item not in duplicates:
#                 duplicates.append(item)
#     return duplicates



# More advanced, with counting the number of times item found in list
def find_duplicates(nums):
    num_counts = {}
    for num in nums:
        num_counts[num] = num_counts.get(num, 0) + 1
 
    duplicates = []
    for num, count in num_counts.items():
        if count > 1:
            duplicates.append(num)
 
    return duplicates


@pytest.mark.parametrize("list1, expected_duplicates", [
    ([4, 3, 2, 7, 8, 2, 3, 1], [3,2]),
    ([], []),
    (["1"], []),
    ([3, 3, 3, 3, 3, 3, 3], [3]),
    (['a', 'b', 'c', 'd', 'd', 'c'], ['c', 'd'])
])
def test_duplicates(list1, expected_duplicates):
    assert find_duplicates(list1) == expected_duplicates
"""
You have been given an array of strings, where each string may contain only lowercase English letters. 
You need to write a function group_anagrams(strings) that groups the anagrams in the array 
together using a hash table (dictionary). 
The function should return a list of lists, where each inner list contains a group of anagrams.

For example, if the input array is ["eat", "tea", "tan", "ate", "nat", "bat"], 
the function should return [["eat","tea","ate"],["tan","nat"],["bat"]] 
because the first three strings are anagrams of each other, 
the next two strings are anagrams of each other, and the last string has no anagrams in the input array.
"""


import pytest


def group_anagrams(strings_list):
    anagrams_groups_dict = {}
    for string in strings_list:
        canonical_string = "".join(sorted(string))
        if canonical_string not in anagrams_groups_dict:
            anagrams_groups_dict[canonical_string] = [string]
        else:
            anagrams_groups_dict[canonical_string].append(string)
    return list(anagrams_groups_dict.values())


print("1st set:")
print( group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"]) )

print("\n2nd set:")
print( group_anagrams(["abc", "cba", "bac", "foo", "bar"]) )

print("\n3rd set:")
print( group_anagrams(["listen", "silent", "triangle", "integral", "garden", "ranged"]) )

"""
    EXPECTED OUTPUT:
    ----------------
    1st set:
    [['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']]

    2nd set:
    [['abc', 'cba', 'bac'], ['foo'], ['bar']]

    3rd set:
    [['listen', 'silent'], ['triangle', 'integral'], ['garden', 'ranged']]

"""

@pytest.mark.parametrize("list_of_strings, expected_anagrams_groups", [
    (["eat", "tea", "tan", "ate", "nat", "bat"], [['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']]),
    (["abc", "cba", "bac", "foo", "bar"], [['abc', 'cba', 'bac'], ['foo'], ['bar']]),
    (["listen", "silent", "triangle", "integral", "garden", "ranged"], [['listen', 'silent'], ['triangle', 'integral'], ['garden', 'ranged']]),
    ([], []),
    (["abc", "def", "ghi"], [["abc"], ["def"], ["ghi"]]),
    (["number"], [["number"]])
])
def test_anagrams_groups(list_of_strings, expected_anagrams_groups):
    assert group_anagrams(list_of_strings) == expected_anagrams_groups
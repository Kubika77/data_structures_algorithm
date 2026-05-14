"""
You have been given a string of lowercase letters.

Write a function called first_non_repeating_char(string) that finds the first non-repeating 
character in the given string using a hash table (dictionary). 
If there is no non-repeating character in the string, the function should return None.
"""


import pytest


def first_non_repeating_char(word):
    chars_dict = {}
    for char in word:
        chars_dict[char] = chars_dict.get(char, 0) + 1
    for char in word:
        if chars_dict[char] == 1:
            return char
    return None


# word = "hello"
# char = first_non_repeating_char(word)

@pytest.mark.parametrize("input_string, expected_non_repeat_char", [
    ("hello", "h"),
    ("leetcode", "l"),
    ("aabbcd", "c"),
    ("aabbcc", None),
    ("", None),
    ("a", "a"),
    ("aa1bb", "1"),
    ("11  23", "2"),
    ("!!@@#$", "#")
])
def test_first_non_repeating_char(input_string, expected_non_repeat_char):
    assert first_non_repeating_char(input_string) == expected_non_repeat_char
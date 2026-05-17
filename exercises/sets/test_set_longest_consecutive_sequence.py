"""
Given an unsorted array of integers, write a function that finds the length of the  
longest_consecutive_sequence 
(i.e., sequence of integers in which each element is one greater than the previous element).

Use sets to optimize the runtime of your solution.

Input: An unsorted array of integers, nums.

Output: An integer representing the length of the longest consecutive sequence in nums.

Example:

Input: nums = [100, 4, 200, 1, 3, 2]
Output: 4
Explanation: The longest consecutive sequence in the input array is [4, 3, 2, 1], and its length is 4.
"""

def longest_consecutive_sequence(arr1):
    set1 = set(arr1)
    longest_seq = 0
    for num in set1:
        if num - 1 not in set1:
            current_num = num
            current_seq = 1
            while current_num + 1 in set1:
                current_seq += 1
                current_num += 1
            
            longest_seq = max(longest_seq, current_seq)
    return longest_seq





print( longest_consecutive_sequence([100, 4, 200, 1, 3, 2]) )



"""
    EXPECTED OUTPUT:
    ----------------
    4

"""
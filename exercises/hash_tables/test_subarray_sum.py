"""
Given an array of integers nums and a target integer target, 
write a Python function called subarray_sum that finds the indices of a contiguous subarray in nums 
that add up to the target sum using a hash table (dictionary).

Your function should take two arguments:
nums: a list of integers representing the input array
target: an integer representing the target sum

Your function should return a list of two integers representing the starting and ending indices
of the subarray that adds up to the target sum. 
If there is no such subarray, your function should return an empty list.

For example:
nums = [1, 2, 3, 4, 5]
target = 9
print(subarray_sum(nums, target))  # should print [1, 3]
"""

def subarray_sum(nums, target):
    current_sum =0
    prefix_sum = {
        0: -1
    }
    for idx, num in enumerate(nums):
        current_sum = current_sum + num
        needed = current_sum - target
        if needed in prefix_sum:
            return [prefix_sum[needed] + 1, idx]
        prefix_sum[current_sum] = idx
    return []




nums = [1, 2, 3, 4, 5]
target = 9
print ( subarray_sum(nums, target) )

nums = [-1, 2, 3, -4, 5]
target = 0
print ( subarray_sum(nums, target) )

nums = [2, 3, 4, 5, 6]
target = 3
print ( subarray_sum(nums, target) )

nums = []
target = 0
print ( subarray_sum(nums, target) )



"""
    EXPECTED OUTPUT:
    ----------------
    [1, 3]
    [0, 3]
    [1, 1]
    []

"""

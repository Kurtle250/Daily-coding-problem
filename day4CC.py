"""
Given an array of integers, find the first missing positive integer in
linear time and constant space. In other words, find the lowest
positive integer that does not exist in the array. The array
can contain duplicates and negative numbers as well.

For example, the input [3, 4, -1, 1] should give 2.
The input [1, 2, 0] should give 3.
"""

def arraychecking(nums):
    if nums is None:
        return 1

    nums.append(0)
    n = len(nums)
    for i in range(n):
        if nums[i] <= 0 or nums[i] >= n:
            nums[i] = 0

    for i in range(n):
        nums[nums[i]%n]+= n

    for i in range(1,n):
        if nums[i]/n == 0:
            return i
    return n

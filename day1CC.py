"""
Given a list of numbers and a number k, return whether any two
numbers fromthe list add up to k.

For example, given [10, 15, 3, 7] and k of 17,
return true since 10 + 7 is 17.

Bonus: Can you do this in one pass?
"""
test_case = [10, 15, 3, 7]

def check_Sum(nums, target):
    if nums == None:
        return [-1,-1]

    visited = []
    for val in nums:
        if (target-val) in visited:
            return True;
        else:
            visited.append(val)


if check_Sum(test_case, 20):
    print ("the sum was found")
else:
    print ("the sum was not found")

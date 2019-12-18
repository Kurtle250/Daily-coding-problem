"""
Given an array of integers, return a new array such that each element
at index i of the new array is the product of all the numbers in the
original array except the one at i.

For example, if our input was [1, 2, 3, 4, 5], the expected output
would be [120, 60, 40, 30, 24]. If our input was [3, 2, 1], the
expected output would be [2, 3, 6].

Follow-up: what if you can't use division?
"""
# test case
lst1 = [3,2,1]
lst2 = [1,2,3,4,5,6,7,8,9]

def sumofproducts(lst):
    if list is None:
        return []

    output = [1]
    next = 1
    for i in range(1,len(lst)):
        next*=lst[i-1]
        output.append(next)

    next = 1
    for i in range(len(lst)-2,-1,-1):
        next*=lst[i+1]
        output[i] = output[i]*next

    return output


print (sumofproducts(lst2))

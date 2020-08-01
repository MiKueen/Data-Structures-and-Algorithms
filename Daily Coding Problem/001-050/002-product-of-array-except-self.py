'''
Author : MiKueen
Level : Medium
Company : Uber
Problem Statement : Product of Array Except Self

Given an array of integers, return a new array such that each element at index i of the new array is the product of all the numbers in the original array except the one at i.
For example, if our input was [1, 2, 3, 4, 5], the expected output would be [120, 60, 40, 30, 24]. If our input was [3, 2, 1], the expected output would be [2, 3, 6].

Follow-up: what if you can't use division?
'''

def productExceptSelf(nums):
    """
    :type nums: List[int]
    :rtype: List[int]
    """
    # Time Complexity - O(n)
    # Space Complexity - O(1)
    res = [1] * len(nums)
    left = right = 1

    for i in range(len(nums)):
        j = -(i+1)
        res[i] *= left 
        res[j] *= right
        left *= nums[i]
        right *= nums[j]       
                
    return res

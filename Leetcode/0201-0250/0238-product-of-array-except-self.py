'''
Author : MiKueen
Level : Medium
Problem Statement : Product of Array Except Self

Given an array nums of n integers where n > 1, return an array output such that output[i] is equal to the product of all the elements of nums except nums[i].

Example:
Input:  [1,2,3,4]
Output: [24,12,8,6]

Constraint: It's guaranteed that the product of the elements of any prefix or suffix of the array (including the whole array) fits in a 32 bit integer.

Note: Please solve it without division and in O(n).

Follow up:
Could you solve it with constant space complexity? (The output array does not count as extra space for the purpose of space complexity analysis.)
'''

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:      
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

'''
Author : MiKueen
Level : Easy 
Problem Statement : Move Zeroes

Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Example:
Input: [0,1,0,3,12]
Output: [1,3,12,0,0]
Note:

You must do this in-place without making a copy of the array.
Minimize the total number of operations.
'''

class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        
        # Method 1
        # Pythonic Way
        cnt = nums.count(0)
        nums[:] = [i for i in nums if i != 0]
        nums += [0] * cnt
        
        # Method 2
        if nums and len(nums) > 1:
            j = 0
            for i in range(len(nums)):
                if nums[i]:
                    if not nums[j]: # check if necessary to swap
                        nums[i], nums[j] = nums[j], nums[i]
                    j += 1

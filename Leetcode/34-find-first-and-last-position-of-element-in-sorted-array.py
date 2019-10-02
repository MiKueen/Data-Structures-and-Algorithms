'''
Author : MiKueen
Level : Medium
Problem Statement : Find First and Last Position of Elements in Sorted Array

Given an array of integers nums sorted in ascending order, find the starting and ending position of a given target value.
Your algorithm's runtime complexity must be in the order of O(log n).
If the target is not found in the array, return [-1, -1].

Example 1:
Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]

Example 2:
Input: nums = [5,7,7,8,8,10], target = 6
Output: [-1,-1]
'''

class Solution:
    def searchLeft(self, nums, target):
        low, high = 0, len(nums) - 1
        while low <= high:
            mid = (low + high) // 2
            if target > nums[mid]: 
                low = mid + 1
            else: 
                high = mid - 1
        return low

    def searchRight(self, nums, target):
        low, high = 0, len(nums) - 1
        while low <= high:
            mid = (low + high) // 2
            if target >= nums[mid]: 
                low = mid + 1
            else: 
                high = mid - 1
        return high
    
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        left_res = self.searchLeft(nums, target)
        right_res = self.searchRight(nums, target)

        if left_res <= right_res:
            return (left_res, right_res)
        else:
            return [-1, -1]
    
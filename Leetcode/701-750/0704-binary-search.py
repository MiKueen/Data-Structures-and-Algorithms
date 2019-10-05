'''
Author : MiKueen
Level : Easy
Problem Statement : Binary Search

Given a sorted (in ascending order) integer array nums of n elements and a target value, write a function to search target in nums. If target exists, then return its index, otherwise return -1.

Example 1:
Input: nums = [-1,0,3,5,9,12], target = 9
Output: 4
Explanation: 9 exists in nums and its index is 4

Example 2:
Input: nums = [-1,0,3,5,9,12], target = 2
Output: -1
Explanation: 2 does not exist in nums so return -1
'''

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if not nums or len(nums) == 0:
            return -1
        low , high = 0 , len(nums) - 1
        if target < nums[low] or target > nums[high]:
            return -1
        while low <= high:
            mid = (low + high)//2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                high = mid - 1
            else:
                low = low + 1
        return -1
        
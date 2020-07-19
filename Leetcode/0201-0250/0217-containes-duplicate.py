'''
Author : MiKueen
Level : Easy
Problem Statement : Contains Duplicate

Given an array of integers, find if the array contains any duplicates.
Your function should return true if any value appears at least twice in the array, and it should return false if every element is distinct.

Example 1:
Input: [1,2,3,1]
Output: true

Example 2:
Input: [1,2,3,4]
Output: false

Example 3:
Input: [1,1,1,3,3,4,3,2,4,2]
Output: true
'''

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        
        # Method 1 : Using Dictionary
        # Time Complexity - O(n), Space Complexity - O(n)
        mapping = {}
        for num in nums:
            if num in mapping:
                return True
            else:
                mapping[num] = 1
        return False
    
        # Method 2 : Using set
        # Time Complexity - O(n), Space Complexity - O(n)
        return len(set(nums)) < len(nums)
        
        # Method 3 : Sorting
        # Time Complexity - O(nlog(n)), Space Complexity - O(1)
        nums.sort()
        for i in range(1, len(nums)):
            if nums[i] == nums[i-1]:
                return True
        return False
        
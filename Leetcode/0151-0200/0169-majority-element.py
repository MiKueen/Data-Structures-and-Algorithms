'''
Author : MiKueen
Level : Easy
Problem Statement : Majority Element

Given an array of size n, find the majority element. The majority element is the element that appears more than ⌊ n/2 ⌋ times.
You may assume that the array is non-empty and the majority element always exist in the array.

Example 1:
Input: [3,2,3]
Output: 3

Example 2:
Input: [2,2,1,1,1,2,2]
Output: 2
'''

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        mapping = {}
        for i in nums:
            if i not in mapping:
                mapping[i] = 1
            if mapping[i] > len(nums) // 2:
                return i
            else:
                mapping[i] += 1 
                
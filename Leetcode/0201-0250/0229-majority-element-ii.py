'''
Author : MiKueen
Level : Medium
Problem Statement : Majority Element II

Given an integer array of size n, find all elements that appear more than ⌊ n/3 ⌋ times.
Note: The algorithm should run in linear time and in O(1) space.

Example 1:
Input: [3,2,3]
Output: [3]

Example 2:
Input: [1,1,1,3,3,2,2,2]
Output: [1,2]
'''

class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        if not nums:
            return []
        
        # Using Majority Voting Algorithm
        # As there can be at most 2 majority elements which are more than n/3
        num1 = num2 = cnt1 = cnt2 = 0
        res = []
        
        for i in nums:
            if i == num1:
                cnt1 += 1
            elif i == num2:
                cnt2 += 1
            elif cnt1 == 0:
                num1 = i
                cnt1 = 1
            elif cnt2 == 0:
                num2 = i
                cnt2 = 1
            else:
                cnt1 -= 1
                cnt2 -= 1
                
        cnt1 = cnt2 = 0
        
        for i in nums:
            if i == num1:
                cnt1 += 1
            elif i == num2:
                cnt2 += 1
                
        if cnt1 > len(nums) // 3:
            res.append(num1)
        if cnt2 > len(nums) // 3:
            res.append(num2)
            
        return res
        
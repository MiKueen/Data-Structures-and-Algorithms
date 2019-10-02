'''
Author : MiKueen
Level : Medium
Problem Statement : 3Sum Closet

Given an array nums of n integers and an integer target, find three integers in nums such that the sum is closest to target. Return the sum of the three integers. You may assume that each input would have exactly one solution.

Example:
Given array nums = [-1, 2, 1, -4], and target = 1.
The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
'''

class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        ans = sum(nums[:3])
        
        for i in range(len(nums)-2):
            k = len(nums)-1 
            j = i + 1 
          
            while j < k:
                close_sum = nums[i] + nums[j] + nums[k]
                
                if close_sum == target:
                    return close_sum
                
                if abs(close_sum - target) < abs(ans - target):
                    ans = close_sum
                
                if close_sum < target:
                    j += 1
                elif close_sum > target: 
                    k -= 1
                else: 
                    break
                          
        return ans
        
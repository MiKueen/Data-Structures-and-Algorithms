'''
Author : MiKueen
Level : Medium
Problem Statement : 4Sum

Given an array nums of n integers and an integer target, are there elements a, b, c, and d in nums such that a + b + c + d = target? Find all unique quadruplets in the array which gives the sum of target.

Note:
The solution set must not contain duplicate quadruplets.

Example:
Given array nums = [1, 0, -1, 0, -2, 2], and target = 0.
A solution set is:
[
  [-1,  0, 0, 1],
  [-2, -1, 1, 2],
  [-2,  0, 0, 2]
]
'''

class Solution:
    # Using 3Sum
    def threeSum(self, nums, target): 
        res = []
        for i in range(len(nums)-2):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            k = len(nums)-1 
            j = i + 1 
            t = target - nums[i]
            while j < k:
                two_sum = nums[j] + nums[k]
                if two_sum == t: 
                    res.append([nums[i], nums[j], nums[k]])
                    while j < k and nums[j] == nums[j+1]:
                        j += 1
                    while j < k and nums[k] == nums[k-1]:
                        k -= 1
                    j += 1
                    k -= 1  
                elif two_sum < t:
                    j += 1
                else: 
                    k -= 1
        return res
    
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        nums.sort()
        for i in range(len(nums)-3):
            if i == 0 or nums[i] != nums[i-1]:
                threeSum_res = self.threeSum(nums[i+1:], target-nums[i])
                for trip in threeSum_res:
                    res.append([nums[i]] + trip)
        return res
        
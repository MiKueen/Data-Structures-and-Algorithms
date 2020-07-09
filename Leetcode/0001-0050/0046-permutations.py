'''
Author : MiKueen
Level : Medium
Problem Statement : Permutations

Given a collection of distinct integers, return all possible permutations.

Example:
Input: [1,2,3]
Output:
[
  [1,2,3],
  [1,3,2],
  [2,1,3],
  [2,3,1],
  [3,1,2],
  [3,2,1]
]
'''

class Solution:
    def helper(self, start, end, nums, res):
        if start == end:
            res.append(nums[:])
        for i in range(start, end):
            nums[start], nums[i] = nums[i], nums[start]
            self.helper(start+1, end, nums, res)
            nums[start], nums[i] = nums[i], nums[start]
                
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        self.helper(0, len(nums), nums, res)
        return res
        
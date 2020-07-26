'''
Author : MiKueen
Level : Medium
Problem Statement : Maximum Product Subarray

Given an integer array nums, find the contiguous subarray within an array (containing at least one number) which has the largest product.

Example 1:
Input: [2,3,-2,4]
Output: 6
Explanation: [2,3] has the largest product 6.

Example 2:
Input: [-2,0,-1]
Output: 0
Explanation: The result cannot be 2, because [-2,-1] is not a subarray.
'''

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # Using Kadane's algorithm
        if not nums:
            return 0
        max_prod = prev_max = prev_min =  nums[0] 
        for i in range(1, len(nums)): 
            curr_min = min(prev_max * nums[i], prev_min * nums[i], nums[i]) 
            curr_max = max(prev_max * nums[i], prev_min * nums[i], nums[i])
            prev_min, prev_max = curr_min, curr_max
            max_prod = max(curr_max, max_prod)    
        return max_prod
        
'''
Author : MiKueen
Level : Medium
Problem Statement : Longest Increasing Subsequence

Given an unsorted array of integers, find the length of longest increasing subsequence.

Example:
Input: [10,9,2,5,3,7,101,18]
Output: 4 
Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4.
'''

class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        
        # DP Solution
        n = len(nums)
        dp = [0] * n
        dp[0] = 1

        for i in range(1, n):
            curr_max = 0
            for j in range(i): 
                if nums[j] < nums[i] and curr_max < dp[j]:
                    curr_max = dp[j]
            dp[i] = curr_max + 1
        return max(dp)
    
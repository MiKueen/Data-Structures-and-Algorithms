'''
Author : MiKueen
Level : Medium
Problem Statement : Subarray Sum Equals K

Given an array of integers and an integer k, you need to find the total number of continuous subarrays whose sum equals to k.

Example 1:
Input:nums = [1,1,1], k = 2
Output: 2
 
Constraints:
The length of the array is in range [1, 20,000].
The range of numbers in the array is [-1000, 1000] and the range of the integer k is [-1e7, 1e7].
'''

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        # Time Complexity - O(n)
        # Space Complexity - O(n)
        curr_sum = res = 0
        mapping = defaultdict(int)
        for i in nums:
            curr_sum += i
            if (curr_sum - k) in mapping:
                res += mapping[curr_sum - k]
            mapping[curr_sum] += 1
        res += mapping[k]
        return res
        
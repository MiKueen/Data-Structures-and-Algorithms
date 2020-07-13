'''
Author : MiKueen
Level : Hard
Problem Statement : Longest Consecutive Sequence

Given an unsorted array of integers, find the length of the longest consecutive elements sequence.

Your algorithm should run in O(n) complexity.

Example:

Input: [100, 4, 200, 1, 3, 2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.
'''

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) <=1 :
            return len(nums)
        nums = set(nums)
        max_seq = 0
        for n in nums:
            if n-1 not in nums:
                temp = n
                cur_seq = 1
                while temp+1 in nums:
                    temp += 1
                    cur_seq += 1
                max_seq = max(max_seq, cur_seq)
        return max_seq
        
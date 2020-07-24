'''
Author : MiKueen
Level : Medium
Problem Statement : Single Number III

Given an array of numbers nums, in which exactly two elements appear only once and all the other elements appear exactly twice. Find the two elements that appear only once.

Example:
Input:  [1,2,1,3,2,5]
Output: [3,5]
Note:

The order of the result is not important. So in the above example, [5, 3] is also correct.
Your algorithm should run in linear runtime complexity. Could you implement it using only constant space complexity?
'''

class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        res = set()
        for i in nums:
            if i in res:
                res.remove(i)
            else:
                res.add(i)
        return res
    
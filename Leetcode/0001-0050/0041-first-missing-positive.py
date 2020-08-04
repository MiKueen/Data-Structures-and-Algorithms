'''
Author : MiKueen
Level : Hard
Problem Statement : First Missing Positive

Given an unsorted integer array, find the smallest missing positive integer.

Example 1:
Input: [1,2,0]
Output: 3

Example 2:
Input: [3,4,-1,1]
Output: 2

Example 3:
Input: [7,8,9,11,12]
Output: 1

Note:
Your algorithm should run in O(n) time and uses constant extra space.
'''

class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        '''
        # Method 1
        # mark those elements who aren't in the range of [1, n]
        n = len(nums)
        for i in range(n):
            if nums[i] <= 0 or nums[i] > n:
                nums[i] = n + 1
        
        # mark visited elements as negative
        for i in range(n): 
            if (abs(nums[i]) - 1 < n and nums[abs(nums[i]) - 1] > 0): 
                nums[abs(nums[i]) - 1] = -nums[abs(nums[i]) - 1] 

        # find first positive/unmarked element and return its index
        for i in range(n): 
            if (nums[i] > 0): 
                return i + 1
        
        # if all elements are negative/marked means all elements are in the range of [1, n]
        return n + 1
        '''
        
        # Method 2
        n = len(nums)
        for i in range(n):
            pos = nums[i] - 1
            while 1 <= nums[i] <= n and nums[i] != nums[pos]:
                nums[i], nums[pos] = nums[pos], nums[i]
                pos = nums[i] - 1
        
        for i in range(n):
            if nums[i] != i + 1:
                return i + 1
        return n + 1
        
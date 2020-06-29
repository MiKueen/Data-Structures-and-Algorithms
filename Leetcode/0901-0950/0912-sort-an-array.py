'''
Author : MiKueen
Level : Medium
Problem Statement : Sort an Array

Given an array of integers nums, sort the array in ascending order.

Example 1:
Input: nums = [5,2,3,1]
Output: [1,2,3,5]

Example 2:
Input: nums = [5,1,1,2,0,0]
Output: [0,0,1,1,2,5]
 
Constraints:
1 <= nums.length <= 50000
-50000 <= nums[i] <= 50000
'''

# Using Merge Sort
# Time Complexity - O(nlog(n))   
# Space Complexity - O(n)

class Solution:     
    def mergeArray(self, left, right, nums):
        l, r = len(left), len(right)
        i = j = k = 0

        while i < l and j < r:
            if left[i] <= right[j]:
                nums[k] = left[i]
                i += 1
            else:
                nums[k] = right[j]
                j += 1
            k += 1

        while i < l:
            nums[k] = left[i]
            i += 1
            k += 1
        while j < r:
            nums[k] = right[j]
            j += 1
            k += 1

        return nums
    
    def sortArray(self, nums: List[int]) -> List[int]:
        if len(nums) < 2:
            return nums
        n = len(nums)
        mid = n // 2
        left, right = nums[:mid], nums[mid:]

        self.sortArray(left)
        self.sortArray(right)
        self.mergeArray(left, right, nums)

        return nums
            
'''
Author : MiKueen
Level : Hard
Problem Statement : Median of Two Sorted Arrays

There are two sorted arrays nums1 and nums2 of size m and n respectively.
Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).
You may assume nums1 and nums2 cannot be both empty.

Example 1:
nums1 = [1, 3]
nums2 = [2]
The median is 2.0

Example 2:
nums1 = [1, 2]
nums2 = [3, 4]
The median is (2 + 3)/2 = 2.5
'''

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:   
        # Binary Search Solution
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        
        x = len(nums1)
        y = len(nums2)
        low = 0
        high = x
        
        while low <= high:
            leftArr = (low + high)//2
            rightArr = (x + y + 1)//2 - leftArr

            maxLeftX = float("-inf") if leftArr == 0 else nums1[leftArr - 1]
            minRightX = float("inf") if leftArr == x else nums1[leftArr]
            maxLeftY = float("-inf") if rightArr == 0 else nums2[rightArr - 1]
            minRightY = float("inf") if rightArr == y else nums2[rightArr]
            
            if (maxLeftX <= minRightY) and (maxLeftY <= minRightX): 
                if ((x + y) % 2 != 0):
                    return max(maxLeftX, maxLeftY)
                else:
                    return (max(maxLeftX, maxLeftY) + min(minRightX, minRightY))/2
            
            elif maxLeftX > minRightY: 
                high = leftArr - 1
            elif maxLeftY > minRightX:
                low = leftArr + 1
        
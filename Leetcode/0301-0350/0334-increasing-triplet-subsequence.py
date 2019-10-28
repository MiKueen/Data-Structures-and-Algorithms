'''
Author : MiKueen
Level : Medium
Problem Statement : Increasing Triplet Subsequence

Given an unsorted array return whether an increasing subsequence of length 3 exists or not in the array.
Formally the function should:
Return true if there exists i, j, k
such that arr[i] < arr[j] < arr[k] given 0 ≤ i < j < k ≤ n-1 else return false.
Note: Your algorithm should run in O(n) time complexity and O(1) space complexity.

Example 1:
Input: [1,2,3,4,5]
Output: true

Example 2:
Input: [5,4,3,2,1]
Output: false

Approach :
1) Initially result = [max, max], we use a list of length 2 to store the subsequence, or smaller value which may form the new subsequence.
2) Traverse the array：
    a) if element <= result[0], then we update res[0] = element.
    b) else if result[0] < element <= result[1], the we update result[1] = element.
    c) else: result[1] < element, we found a subsequence of length 3, return true. 
'''

class Solution(object):
    def increasingTriplet(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        res = [float('inf'), float('inf')]
        for ele in nums:
            if ele <= res[0]:
                res[0] = ele
            elif ele <= res[1]:
                res[1] = ele
            else:
                return True
        return False
    
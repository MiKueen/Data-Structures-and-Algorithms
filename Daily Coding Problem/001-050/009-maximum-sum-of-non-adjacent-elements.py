'''
Author : MiKueen
Level : Medium
Company : Airbnb
Problem Statement : Maximum Sum of Non-Adjacent Elements

Given a list of integers, write a function that returns the largest sum of non-adjacent numbers. Numbers can be 0 or negative.
For example, [2, 4, 6, 2, 5] should return 13, since we pick 2, 6, and 5. [5, 1, 1, 5] should return 10, since we pick 5 and 5.
Follow-up: Can you do this in O(N) time and constant space?
'''

def maxSumNonAdjacent(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    
    if not nums:
        return 0
    if len(nums) == 1:
        return nums
    if len(nums) == 2:
        return max(nums[0], nums[1])

    # Time Complexity - O(n)
    # Space Complexity - O(1)
    
    first, second = nums[0], nums[1]

    for i in range(2, len(nums)):
        curr = first + nums[i]
        first, second = max(first, second), curr

    return max(first, second)

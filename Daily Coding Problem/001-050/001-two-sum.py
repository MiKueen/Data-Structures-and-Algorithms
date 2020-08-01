'''
Author : MiKueen
Level : Easy
Company : Google
Problem Statement : Two Sum

Given a list of numbers and a number k, return whether any two numbers from the list add up to k.
For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.

Bonus: Can you do this in one pass?
'''

def twoSum(nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: bool
    """
    # Time Complexity - O(n)
    # Space Complexity - O(n)
    res = set()
    for i in nums:
        if i in res:
            return True
        res.add(k - i)
    return False

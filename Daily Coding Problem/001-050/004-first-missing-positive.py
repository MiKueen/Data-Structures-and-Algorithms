'''
Author : MiKueen
Level : Hard
Company : Stripe
Problem Statement : First Missing Positive

Given an array of integers, find the first missing positive integer in linear time and constant space. 
In other words, find the lowest positive integer that does not exist in the array. 
The array can contain duplicates and negative numbers as well.

For example, the input [3, 4, -1, 1] should give 2. The input [1, 2, 0] should give 3.

You can modify the input array in-place.
'''

def firstMissingPositive(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    
    # Method 1: Changing array values
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
    # Method 2: Changing position of elements
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
    '''
    
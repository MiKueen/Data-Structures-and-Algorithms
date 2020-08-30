'''
Author : MiKueen
Level : Medium
Problem Statement : Largest Number

Given a list of non negative integers, arrange them such that they form the largest number.

Example 1:
Input: [10,2]
Output: "210"

Example 2:
Input: [3,30,34,5,9]
Output: "9534330"

Note: The result may be very large, so you need to return a string instead of an integer.
'''

class Solution:
    def compareDigits(self, digit, max_digit):
        if digit + max_digit >= max_digit + digit:
            return True
        return False
    
    def largestNumber(self, nums: List[int]) -> str:
        res = ""
        while nums:
            max_digit = float('-inf')
            for d in nums:
                if max_digit < 0 or self.compareDigits(str(d), str(max_digit)):
                    max_digit = d
            res += str(max_digit)
            nums.remove(max_digit)
        if res[0] == '0':
            return '0'
        else:
            return res
    
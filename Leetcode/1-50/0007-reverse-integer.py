'''
Author : MiKueen
Level : Easy
Problem Statement : Reverse Integer

Given a 32-bit signed integer, reverse digits of an integer.

Example 1:
Input: 123
Output: 321

Example 2:
Input: -123
Output: -321

Example 3:
Input: 120
Output: 21
'''

class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x < 0:
            ans = int ('-'+str(x)[::-1][:-1])
        else:
            ans = int(str(x)[::-1])
        return ans if ans in range(-2**31, (2**31)-1) else 0
        
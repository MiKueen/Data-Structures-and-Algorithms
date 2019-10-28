'''
Author : MiKueen
Level : Medium
Problem Statement : Count Numbers with Unique Digits

Given a non-negative integer n, count all numbers with unique digits, x, where 0 ≤ x < 10n.

Example:
Input: 2
Output: 91 
Explanation: The answer should be the total numbers in the range of 0 ≤ x < 100, 
             excluding 11,22,33,44,55,66,77,88,99
'''

class Solution(object):
    def countNumbersWithUniqueDigits(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0: 
            return 1
        if n == 1: 
            return 10
        
        # res initially stores number 1,2,...,9 and 10^n
        res = 10
        # number of choices for the leading digit (which is 1,2,...,9)
        choices = 9
        for i in range(1, n):
            choices = choices * (10 - i)    
            res += choices
        return res
        
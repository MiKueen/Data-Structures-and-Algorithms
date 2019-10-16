'''
Author : MiKueen
Level : Medium
Problem Statement : Divide Two Integers

Given two integers dividend and divisor, divide two integers without using multiplication, division and mod operator.
Return the quotient after dividing dividend by divisor.
The integer division should truncate toward zero.

Example 1:
Input: dividend = 10, divisor = 3
Output: 3

Example 2:
Input: dividend = 7, divisor = -3
Output: -2
'''

class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        s = (-1 if((dividend < 0) ^ (divisor < 0)) else 1)
        
        dividend, divisor = abs(dividend), abs(divisor)
        res = q = 0
        
        while dividend >= divisor:
            temp, i = divisor, 1
            while dividend >= temp:
                dividend -= temp
                res += i
                i <<= 1
                temp <<= 1
            
        if s == 1:
            return min(2147483647, res)
        else:
            return max(-2147483648, 0-res)
    
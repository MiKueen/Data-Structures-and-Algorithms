'''
Author : MiKueen
Level : Medium
Problem Statement : Integer Break

Given a positive integer n, break it into the sum of at least two positive integers and maximize the product of those integers. Return the maximum product you can get.

Example 1:
Input: 2
Output: 1
Explanation: 2 = 1 + 1, 1 × 1 = 1.

Example 2:
Input: 10
Output: 36
Explanation: 10 = 3 + 3 + 4, 3 × 3 × 4 = 36.
'''

class Solution(object):
    def integerBreak(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 2 or n == 3:
            return n-1
        
        res = 1
        while n > 4:
            res *= 3
            n -= 3
        res *= n
        return res
    
        
        '''
        # DP Solution
        dp = [1]
        for m in range (2, n + 1):
            j = m - 1
            i = 1
            max_prod = 0
            while i <= j:
                max_prod = max(max_prod, max(i, dp[i-1]) * max(j, dp[j-1]))
                j -= 1
                i += 1
            dp.append(max_prod)
        return dp[n-1]
        '''
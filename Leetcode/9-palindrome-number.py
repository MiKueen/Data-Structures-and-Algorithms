'''
Author : MiKueen
Level : Easy
Problem Statement : Palindrome Number

Determine whether an integer is a palindrome. An integer is a palindrome when it reads the same backward as forward.

Example 1:
Input: 121
Output: true

Example 2:
Input: -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.

Example 3:
Input: 10
Output: false
Explanation: Reads 01 from right to left. Therefore it is not a palindrome.
'''

class Solution:
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        
        if x < 0:
            return False
        else:
            return str(x)[::-1] == str(x)
        
        '''
        # Another solution by extracting digits

        if x == 0:
            return True
        elif x < 0 or x % 10 == 0:
            return False
        if x < 10:
            return True
        
        temp, rev = x, 0
        while x > 0:
            pop = x % 10
            rev = rev * 10 + pop
            x = x // 10
        
        if temp == rev:
            return True
        else:
            return False
        '''
        
'''
Author : MiKueen
Level : Medium
Problem Statement : Longest Palindromic Substring

Given a string s, find the longest palindromic substring in s. 
You may assume that the maximum length of s is 1000.

Example 1:
Input: "babad"
Output: "bab"

Note: "aba" is also a valid answer.

Example 2:
Input: "cbbd"
Output: "bb"
'''

class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        res = [[False] * len(s) for i in range(len(s))]
        max_sublen = 0
        max_indice = (0,0)
        
        for j in range(len(s)):
            for i in range(j+1):
                res[i][j] = s[i] == s[j] and (j - i < 2 or res[i+1][j-1])
                if res[i][j] and max_sublen < j - i + 1:
                    max_sublen = j - i + 1
                    max_indice = (i,j)
        
        return s[max_indice[0]:max_indice[1]+1]
    
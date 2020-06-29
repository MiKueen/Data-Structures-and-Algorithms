'''
Author : MiKueen
Level : Easy
Problem Statement : First Unique Character in a String

Given a string, find the first non-repeating character in it and return its index. 
If it doesn't exist, return -1.

Examples:

s = "leetcode"
return 0.

s = "loveleetcode"
return 2.
 
Note: You may assume the string contains only lowercase English letters.
'''

class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        mapping = {}
        for char in s:
            if char in mapping.keys():
                mapping[char] += 1
            else:
                mapping[char] = 1
                
        for i in range(len(s)):
            if mapping[s[i]] == 1:
                return i    
        return -1
    
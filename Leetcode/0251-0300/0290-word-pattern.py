'''
Author : MiKueen
Level : Easy
Problem Statement : Word Pattern

Given a pattern and a string str, find if str follows the same pattern.
Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty word in str.

Example 1:
Input: pattern = "abba", str = "dog cat cat dog"
Output: true

Example 2:
Input:pattern = "abba", str = "dog cat cat fish"
Output: false

Example 3:
Input: pattern = "aaaa", str = "dog cat cat dog"
Output: false

Example 4:
Input: pattern = "abba", str = "dog dog dog dog"
Output: false

Notes:
You may assume pattern contains only lowercase letters, and str contains lowercase letters that may be separated by a single space.
'''

class Solution:
    def wordPattern(self, pattern: str, str: str) -> bool:
        if len(pattern) != len(str.split()):
            return False
        
        # Time Complexity - O(n)
        # Space Complexity -O(n)
        words = str.split()
        mapping = {}
        
        for i in range(len(pattern)):
            if pattern[i] not in mapping:
                if words[i] not in mapping.values():
                    mapping[pattern[i]] = words[i]
                else:
                    return False
            else:
                if mapping[pattern[i]] != words[i]:
                    return False
        
        return True
    
'''
Author : MiKueen
Level : Medium
Problem Statement : Longest Substring Without Repeating Characters

Given a string, find the length of the longest substring without repeating characters.

Example 1:
Input: "abcabcbb"
Output: 3 
Explanation: The answer is "abc", with the length of 3. 

Example 2:
Input: "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.

Example 3:
Input: "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3. 
             Note that the answer must be a substring, "pwke" is a subsequence and not a substring.
'''

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        temp = {}
        maxlen = start = 0
        for i, char in enumerate(s):
            if char in temp and start <= temp[char]:
                start = temp[char] + 1
            else:
                maxlen = max(maxlen, i - start + 1)      
            temp[char] = i

        return maxlen
        
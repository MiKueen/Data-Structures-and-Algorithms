'''
Author : MiKueen
Level : Easy
Problem Statement : Longest Palindrome

Given a string which consists of lowercase or uppercase letters, find the length of the longest palindromes that can be built with those letters.
This is case sensitive, for example "Aa" is not considered a palindrome here.

Note:
Assume the length of given string will not exceed 1,010.

Example:
Input:
"abccccdd"
Output:
7
Explanation:
One longest palindrome that can be built is "dccaccd", whose length is 7.
'''

class Solution:
    def longestPalindrome(self, s: str) -> int:
        if len(s) <= 1:
            return len(s)
            
        mapping, res, first_odd = {}, 0, False

        for i in s:
            if i not in mapping:
                mapping[i] = 1
            else:
                mapping[i] += 1

        for i in mapping:
            if mapping[i] % 2 == 0:
                res += mapping[i]
            else:
                if not first_odd:
                    res += mapping[i]
                    first_odd = True
                else:
                    res += mapping[i] - 1

        return res
                
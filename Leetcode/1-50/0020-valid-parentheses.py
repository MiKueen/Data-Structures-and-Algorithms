'''
Author : MiKueen
Level : Easy
Problem Statement : Valid Parentheses

Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
An input string is valid if:
Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Note that an empty string is also considered valid.

Example 1:
Input: "()"
Output: true

Example 2:
Input: "()[]{}"
Output: true

Example 3:
Input: "(]"
Output: false

Example 4:
Input: "([)]"
Output: false

Example 5:
Input: "{[]}"
Output: true
'''

class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if s is None or len(s) % 2 == 1:
            return False 
        mapping = dict(zip('({[', ')}]'))
        stack = []
        
        for char in s:
            if char in mapping:
                stack.append(mapping[char])
            elif not (stack and char == stack.pop()):
                return False

        return not stack

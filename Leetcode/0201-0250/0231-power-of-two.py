'''
Author : MiKueen
Level : Easy
Problem Statement : Power of Two

Given an integer, write a function to determine if it is a power of two.

Example 1:
Input: 1
Output: true 
Explanation: 20 = 1

Example 2:
Input: 16
Output: true
Explanation: 24 = 16

Example 3:
Input: 218
Output: false
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        binary = bin(n).replace("0b","") 
        cnt = binary.count("1")
        return n > 0 and cnt == 1
        
'''
Author : MiKueen
Level : Medium
Problem Statement : Unique Binary Search Trees

Given n, how many structurally unique BST's (binary search trees) that store values 1 ... n?

Example:
Input: 3
Output: 5
Explanation:
Given n = 3, there are a total of 5 unique BST's:

   1         3     3      2      1
    \       /     /      / \      \
     3     2     1      1   3      2
    /     /       \                 \
   2     1         2                 3
'''

class Solution(object):
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        # Catalan Numbers Solution: f(i,n) = g(i-1) + g(n-i)
        if n == 0 or n == 1:
            return 1
        res = [0] * (n+1)
        res[0], res[1] = 1, 1
        for i in range(2,n+1):
            for j in range(1,i+1):
                res[i] += res[j-1] * res[i-j]
        return res[n]
    
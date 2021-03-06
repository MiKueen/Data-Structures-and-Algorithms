'''
Author : MiKueen
Level : Hard
Problem Statement : Binary Tree Maximum Path Sum

Given a non-empty binary tree, find the maximum path sum.
For this problem, a path is defined as any sequence of nodes from some starting node to any node in the tree along the parent-child connections. The path must contain at least one node and does not need to go through the root.

Example 1:
Input: [1,2,3]
       1
      / \
     2   3
Output: 6

Example 2:
Input: [-10,9,20,null,null,15,7]
   -10
   / \
  9  20
    /  \
   15   7
Output: 42
'''

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        # Recursive Solution
        self.res = float('-inf')
        self.helper(root)
        return self.res 
        
    def helper(self, root):
        if not root:
            return 0
        left, right = self.helper(root.left), self.helper(root.right)
        self.res = max(self.res, root.val + left + right)
        return max(root.val + max(left, right), 0)
    
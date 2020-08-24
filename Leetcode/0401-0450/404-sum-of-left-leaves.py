'''
Author : MiKueen
Level : Easy
Problem Statement : Sum of Left Leaves

Find the sum of all left leaves in a given binary tree.

Example:
    3
   / \
  9  20
    /  \
   15   7
There are two left leaves in the binary tree, with values 9 and 15 respectively. Return 24.
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        if not root or (root.left is None and root.right is None):
            return 0
        
        res, stack = 0, [root]
        while stack:
            node = stack.pop()
            if node.left:
                if node.left.left is None and node.left.right is None:
                    res += node.left.val
                else:
                    stack.append(node.left)
            if node.right:
                stack.append(node.right)
        
        return res
    
'''
Author : MiKueen
Level : Easy
Problem Statement : Binary Tree Level Order Traversal II

Given a binary tree, return the bottom-up level order traversal of its nodes' values. (ie, from left to right, level by level from leaf to root).

For example:
Given binary tree [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
return its level order traversal as:
[
  [15,7],
  [9,20],
  [3]
]
'''

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root: 
            return []
        level, res = [root], []
        while level:
            next_level = []
            for i in range(len(level)):
                node = level.pop()
                if node.left:
                    level.insert(0,node.left)
                if node.right:
                    level.insert(0,node.right)
                next_level.append(node.val)
            res.insert(0,next_level)
        return res
        
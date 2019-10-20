'''
Author : MiKueen
Level : Medium
Problem Statement : Binary Search Tree to Greater Sum Tree

Given the root of a binary search tree with distinct values, modify it so that every node has a new value equal to the sum of the values of the original tree that are greater than or equal to node.val.
As a reminder, a binary search tree is a tree that satisfies these constraints:
The left subtree of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees.
 
Example 1:
              4(30)
            /       \
        1(36)      6(21)
       /    \     /     \
    0(36)  2(35) 5(26)  7(15)
            \            \
           3(33)         8(8)

Input: [4,1,6,0,2,5,7,null,null,null,3,null,null,null,8]
Output: [30,36,21,36,35,26,15,null,null,null,33,null,null,null,8]
'''

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def bstToGst(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        stack, res, node = [], 0, root
        while stack or node:
            while node:
                stack.append(node)
                node = node.right
            node = stack.pop()
            res += node.val
            node.val = res
            node = node.left
        return root
    
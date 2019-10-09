'''
Author : MiKueen
Level : Medium
Problem Statement : Construct Binary Tree from Inorder and Postorder Traversal

Given inorder and postorder traversal of a tree, construct the binary tree.
Note:
You may assume that duplicates do not exist in the tree.

For example, given
inorder = [9,3,15,20,7]
postorder = [9,15,7,20,3]
Return the following binary tree:
    3
   / \
  9  20
    /  \
   15   7
'''

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """
        # Recursive Solution
        if not inorder or not postorder:
            return None
        
        # Find index of root node within in-order traversal
        index = inorder.index(postorder.pop())
        root = TreeNode(inorder[index])

        # Recursively generate right subtree starting from 
        # next of root index till last index
        root.right = self.buildTree(inorder[index+1:], postorder)
        
        # Recursively generate left subtree starting from 
        # 0th index to root index within in-order traversal
        root.left = self.buildTree(inorder[:index], postorder)
        return root
        
'''
Author : MiKueen
Level : Medium
Problem Statement : All Elements in Two Binary Search Trees

Given two binary search trees root1 and root2.
Return a list containing all the integers from both trees sorted in ascending order.

Example 1:
Input: root1 = [2,1,4], root2 = [1,0,3]
Output: [0,1,1,2,3,4]

Example 2:
Input: root1 = [0,-10,10], root2 = [5,1,7,0,2]
Output: [-10,0,0,1,2,5,7,10]

Example 3:
Input: root1 = [], root2 = [5,1,7,0,2]
Output: [0,1,2,5,7]

Example 4:
Input: root1 = [0,-10,10], root2 = []
Output: [-10,0,10]

Example 5:
Input: root1 = [1,null,8], root2 = [8,1]
Output: [1,1,8,8]
 
Constraints:
Each tree has at most 5000 nodes.
Each node's value is between [-10^5, 10^5].
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    
    def inorderTraversal(self, root):
        if not root:
            return []
        stack, res = [], []
        while stack or root:
            while root:
                stack.append(root)
                root = root.left
            node = stack.pop()
            res.append(node.val)
            root = node.right 
        return res
    
    def mergeLists(self, res1, res2):
        m, n = len(res1), len(res2)
        res = []
        i = j = 0
        while i < m and j < n:
            if res1[i] <= res2[j]:
                res.append(res1[i])
                i += 1
            else:
                res.append(res2[j])
                j += 1
        return res + res1[i:] + res2[j:]
        
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        if not root1 and not root2:
            return []
        res1 = self.inorderTraversal(root1)
        res2 = self.inorderTraversal(root2)
        return self.mergeLists(res1, res2)
           
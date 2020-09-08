'''
Author : MiKueen
Level : Easy
Problem Statement : Sum of Root to Leaf Binary Numbers

Given a binary tree, each node has value 0 or 1.  Each root-to-leaf path represents a binary number starting with the most significant bit.  
For example, if the path is 0 -> 1 -> 1 -> 0 -> 1, then this could represent 01101 in binary, which is 13.
For all leaves in the tree, consider the numbers represented by the path from the root to that leaf.
Return the sum of these numbers.

Example 1:
Input: [1,0,1,0,1,0,1]
Output: 22
Explanation: (100) + (101) + (110) + (111) = 4 + 5 + 6 + 7 = 22
 
Note:
The number of nodes in the tree is between 1 and 1000.
node.val is 0 or 1.
The answer will not exceed 2^31 - 1.
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def sumRootToLeaf(self, root: TreeNode) -> int:
        if not root:
            return 0
        
        # DFS Solution using Stack
        # Pre Order Traversal
        stack, res = [(root, root.val)], 0
        
        while stack:
            node, value = stack.pop()
            if not node.left and not node.right:
                res += value
            if node.left:
                stack.append((node.left, value * 2 + node.left.val))
            if node.right:
                stack.append((node.right, value * 2 + node.right.val))
                
        return res
    
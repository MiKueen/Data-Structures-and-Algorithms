'''
Author : MiKueen
Level : Medium
Problem Statement : Binary Tree Right Side View

Given a binary tree, imagine yourself standing on the right side of it, return the values of the nodes you can see ordered from top to bottom.

Example:
Input: [1,2,3,null,5,null,4]
Output: [1, 3, 4]
Explanation:

   1            <---
 /   \
2     3         <---
 \     \
  5     4       <---
  '''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        if not root:
            return None
        if root.left is None and root.right is None:
            return [root.val]
        
        # Using Level Order Traversal
        level, res = deque([root]), []
        while level:
            next_level = []
            for i in range(len(level)):
                node = level.popleft()
                if node.left:
                    level.append(node.left)
                if node.right:
                    level.append(node.right)
                next_level.append(node.val)
            # for left side view, uncomment below line
            # res.append(next_level[0])
            res.append(next_level[-1])
        return res
    
'''
Author : MiKueen
Level : Medium
Problem Statement : Path Sum III

You are given a binary tree in which each node contains an integer value.
Find the number of paths that sum to a given value.
The path does not need to start or end at the root or a leaf, but it must go downwards (traveling only from parent nodes to child nodes).
The tree has no more than 1,000 nodes and the values are in the range -1,000,000 to 1,000,000.

Example:
root = [10,5,-3,3,2,null,11,3,-2,null,1], sum = 8

      10
     /  \
    5   -3
   / \    \
  3   2   11
 / \   \
3  -2   1

Return 3. The paths that sum to 8 are:
1.  5 -> 3
2.  5 -> 2 -> 1
3. -3 -> 11
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> int:
        if not root:
            return 0
        
        # Recursive DFS
		# Using Prefix Sum approach
        # Problem 560 follows same approach
        
        def dfs(node, curr_sum, sum):
            if not node:
                return 0
            
            res = 0
            curr_sum += node.val
            
            if (curr_sum - sum) in mapping:
                res += mapping[curr_sum - sum]
            if curr_sum in mapping:
                mapping[curr_sum] += 1
            else:
                mapping[curr_sum] = 1
                
            res += dfs(node.left, curr_sum, sum)
            res += dfs(node.right, curr_sum, sum)
            mapping[curr_sum] -= 1
            
            return res
            
        mapping = defaultdict(int)
        mapping[0] = 1
        return dfs(root, 0, sum)
    
'''
Author : MiKueen
Level : Hard
Problem Statement : Serialize and Deserialize Binary Tree

Serialization is the process of converting a data structure or object into a sequence of bits so that it can be stored in a file or memory buffer, 
or transmitted across a network connection link to be reconstructed later in the same or another computer environment.
Design an algorithm to serialize and deserialize a binary tree. There is no restriction on how your serialization/deserialization algorithm should work. 
You just need to ensure that a binary tree can be serialized to a string and this string can be deserialized to the original tree structure.

Example: 
You may serialize the following tree:
    1
   / \
  2   3
     / \
    4   5
as "[1,2,3,null,null,4,5]"

Clarification: The above format is the same as how LeetCode serializes a binary tree. You do not necessarily need to follow this format, 
so please be creative and come up with different approaches yourself.

Note: Do not use class member/global/static variables to store states. Your serialize and deserialize algorithms should be stateless.
'''

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    # Method 1
    # Recursive DFS (Pre Order Traversal)
    
    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        if not root: 
            return ""
        
        def dfs(node):
            if node is None:
                res.append('None')
                return ""
            res.append(str(node.val))
            dfs(node.left)
            dfs(node.right)

        res = []
        dfs(root)
        return ', '.join(res)
    
    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if not data:
            return None
        
        data = data.split(', ')
        
        def dfs():
            if data[self.i] == 'None':
                self.i += 1
                return None
            root = TreeNode(int(data[self.i]))
            self.i += 1
            root.left = dfs()
            root.right = dfs()
            return root
        
        self.i = 0
        return dfs()
    
    
    # Method 2
    # Iterative BFS (Level Order Traversal)
    
    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        if not root: 
            return ""
    
        level, res = deque([root]), []
        
        while level:
            node = level.popleft()
            
            if node:
                res.append(str(node.val))
                level.append(node.left)
                level.append(node.right)
            else:
                res.append("None")
        
        return ", ".join(res)
    
    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if not data:
            return None
        
        data = data.split(', ')
        root = TreeNode(int(data[0]))
        level = deque([root])
        i = 1
        
        while level:
            node = level.popleft()
            
            if data[i] != 'None':
                node.left = TreeNode(int(data[i]))
                level.append(node.left)
            i += 1
            
            if data[i] != 'None':
                node.right = TreeNode(int(data[i]))
                level.append(node.right)
            i += 1
            
        return root
    

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))

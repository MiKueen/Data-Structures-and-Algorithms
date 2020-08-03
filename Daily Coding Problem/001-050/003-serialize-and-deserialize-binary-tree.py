'''
Author : MiKueen
Level : Hard
Company : Google
Problem Statement : Serialize and Deserialize Binary Tree

Given the root to a binary tree, implement serialize(root), which serializes the tree into a string, and deserialize(s), which deserializes the string back into the tree.

For example, given the following Node class

class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
'''

# Method 1
# Recursive DFS (Pre Order Traversal)

def serialize(root):
    """
    Encodes a tree to a single string.
    
    :type root: Node
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

def deserialize(data):
    """
    Decodes your encoded data to tree.
    
    :type data: str
    :rtype: Node
    """
    if not data:
        return None
    
    data = data.split(', ')
    
    def dfs():
        if data[i[0]] == 'None':
            i[0] += 1
            return None
        root = Node(int(data[i[0]]))
        i[0] += 1
        root.left = dfs()
        root.right = dfs()
        return root
    
    i = [0]
    return dfs()


# Method 2
# Iterative BFS (Level Order Traversal)

def serialize(root):
    """
    Encodes a tree to a single string.
    
    :type root: Node
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

def deserialize(data):
    """
    Decodes your encoded data to tree.
    
    :type data: str
    :rtype: Node
    """
    if not data:
        return None
    
    data = data.split(', ')
    root = Node(int(data[0]))
    level = deque([root])
    i = 1
    
    while level:
        node = level.popleft()
        
        if data[i] != 'None':
            node.left = Node(int(data[i]))
            level.append(node.left)
        i += 1
        
        if data[i] != 'None':
            node.right = Node(int(data[i]))
            level.append(node.right)
        i += 1
        
    return root

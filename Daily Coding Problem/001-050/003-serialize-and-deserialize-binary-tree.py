'''
Author : MiKueen
Level : Hard
Company : Google
Problem Statement : Product of Array Except Self

Given the root to a binary tree, implement serialize(root), which serializes the tree into a string, and deserialize(s), which deserializes the string back into the tree.

For example, given the following Node class

class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
'''

# Using Level Order Traversal

def serialize(root):
    """
    Encodes a tree to a single string.
    
    :type root: Node
    :rtype: str
    """
    if not root: 
        return None
    
    level, res = deque([root]), []
    while level:
        node = level.popleft()
        if node:
            res.append(node.val)
            level.append(node.left)
            level.append(node.right)
        else:
            res.append(None)
            
    while res[-1] is None:
        res.pop()

    return ','.join([str(i) for i in res])
    

def deserialize(data):
    """
    Decodes your encoded data to tree.
    
    :type data: str
    :rtype: Node
    """
    if not data:
        return None
    
    data = data.split(",")
    nodes = deque()
    for i in data:
        if i == "None":
            nodes.append(None)
        else:
            nodes.append(Node(int(i)))

    root = nodes.popleft()
    level = deque([root])

    while nodes and level:
        node = level.popleft()
        node.left = nodes.popleft()
        if nodes:
            node.right = nodes.popleft()
        if node.left:
            level.append(node.left)
        if node.right:
            level.append(node.right)

    return root
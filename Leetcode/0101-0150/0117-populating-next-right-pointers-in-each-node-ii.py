'''
Author : MiKueen
Level : Medium
Problem Statement : Populating Next Right Pointers in Each Node II

Given a binary tree
struct Node {
  int val;
  Node *left;
  Node *right;
  Node *next;
}
Populate each next pointer to point to its next right node. If there is no next right node, the next pointer should be set to NULL.
Initially, all next pointers are set to NULL.

Example:
    1                   1-->Null
   / \                 / \    
  2   3               2-->3-->Null
 / \   \             / \   \
4   5   7           4-->5   7-->Null
   fig A                   fig B

Input: {"$id":"1","left":{"$id":"2","left":{"$id":"3","left":null,"next":null,"right":null,"val":4},
"next":null,"right":{"$id":"4","left":null,"next":null,"right":null,"val":5},"val":2},"next":null,"right":{"$id":"5","left":null,
"next":null,"right":{"$id":"6","left":null,"next":null,"right":null,"val":7},"val":3},"val":1}

Output: {"$id":"1","left":{"$id":"2","left":{"$id":"3","left":null,"next":{"$id":"4","left":null,"next":{"$id":"5","left":null,
"next":null,"right":null,"val":7},"right":null,"val":5},"right":null,"val":4},"next":{"$id":"6","left":null,
"next":null,"right":{"$ref":"5"},"val":3},"right":{"$ref":"4"},"val":2},"next":null,"right":{"$ref":"6"},"val":1}
Explanation: Given the above binary tree (Figure A), your function should populate each next pointer to point to its next right node, just like in Figure B.
 
Note:
You may only use constant extra space.
Recursive approach is fine, implicit stack space does not count as extra space for this problem.
'''

"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, left, right, next):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""
class Solution(object):
    def connect(self, root):
        """
        :type root: Node
        :rtype: Node
        """
        curr = root
        while curr:
            prev = level = Node(0)
            while curr:
                if curr.left:
                    prev.next = curr.left
                    prev = prev.next
                if curr.right:
                    prev.next = curr.right
                    prev = prev.next
                curr = curr.next
            curr = level.next
        return root
        
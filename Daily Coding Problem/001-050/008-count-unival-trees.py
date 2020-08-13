'''
Author : MiKueen
Level : Medium
Company : Google
Problem Statement : Count Unival Subtrees

A unival tree (which stands for "universal value") is a tree where all nodes under it have the same value.
Given the root to a binary tree, count the number of unival subtrees.

For example, the following tree has 5 unival subtrees:
   0
  / \
 1   0
    / \
   1   0
  / \
 1   1
 '''

class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

def check_unival(root):
    if root is None:
        return True
    if root.left is not None and root.left.value != root.value:
        return False
    if root.right is not None and root.right.value != root.value:
        return False
    if check_unival(root.left) and check_unival(root.right):
        return True
    return False

def helper(root):
    if root is None:
        return 0, True

    res_left, check_left = helper(root.left)
    res_right, check_right = helper(root.right)

    check = True
    if not check_left or not check_right:
        check = False
    if root.left is not None and root.left.value != root.value:
        check = False
    if root.right is not None and root.right.value != root.value:
        check = False
    if check:
        return res_left + res_right + 1, True
    else:
        return res_left + res_right, False

def count_univals(root):
    res, check_unival = helper(root)
    return res

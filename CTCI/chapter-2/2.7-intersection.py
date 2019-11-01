'''
Author : MiKueen
Problem Statement : Intersection

Given two (singly) linked lists, determine if the two lists intersect. Return the
intersecting node. Note that the intersection is defined based on reference, not value. That is, if the
kth node of the first linked list is the exact same node (by reference) as the jth node of the second
linked list, then they are intersecting. 
'''

# Time Complexity O(m+n)
# Space Complexity O(1)

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def intersection(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        if headA is None or headB is None:
            return None

        a, b = headA, headB
        
        while a != b:
            a = a.next if a else headB
            b = b.next if b else headA
            
        return a
    
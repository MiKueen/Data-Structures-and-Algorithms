'''
Author : MiKueen
Level : Medium
Problem Statement : Reorder List

Given a singly linked list L: L0→L1→…→Ln-1→Ln,
reorder it to: L0→Ln→L1→Ln-1→L2→Ln-2→…

You may not modify the values in the list's nodes, only nodes itself may be changed.

Example 1:
Given 1->2->3->4, reorder it to 1->4->2->3.

Example 2:
Given 1->2->3->4->5, reorder it to 1->5->2->4->3.
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if head is None or head.next is None:
            return
        
        # Step 1: Find middle element
        slow = fast = head
        while fast and fast.next:
            prev = slow
            slow, fast = slow.next, fast.next.next
        # prev is the last node of first half
        prev.next = None
        
        # Step 2: Reverse second half
        prev, curr = None, slow
        while curr:
            temp, curr.next = curr.next, prev
            prev, curr = curr, temp
        
        # Step 3: Merge both lists
        h1, h2 = head, prev
        # As size of second half >= size of first half
        while h2:
            temp, h1.next = h1.next, h2
            h1, h2 = h2, temp
            
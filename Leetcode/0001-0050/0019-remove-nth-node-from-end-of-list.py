'''
Author : MiKueen
Level : Medium
Problem Statement : Remove Nth Node From End of List

Given a linked list, remove the n-th node from the end of list and return its head.

Example:
Given linked list: 1->2->3->4->5, and n = 2.
After removing the second node from the end, the linked list becomes 1->2->3->5.
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution: 
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        dummy = ListNode(0)
        dummy.next = head
        slow = fast = dummy
        fast = fast.next 
        
        for i in range(n):
            fast = fast.next
        
        while(fast is not None): 
            fast = fast.next 
            slow = slow.next    
        slow.next = slow.next.next
        
        return dummy.next
        
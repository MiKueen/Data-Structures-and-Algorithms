'''
Author : MiKueen
Level : Medium
Problem Statement : Reverse Linked List II

Reverse a linked list from position m to n. Do it in one-pass.
Note: 1 ≤ m ≤ n ≤ length of list.

Example:
Input: 1->2->3->4->5->NULL, m = 2, n = 4
Output: 1->4->3->2->5->NULL
'''

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        if m == n:
            return head

        curr, prev = head, None
        while m > 1:
            prev = curr
            curr = curr.next
            m, n = m-1, n-1

        tail, ptr = curr, prev
        while n:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
            n -= 1

        if ptr:
            ptr.next = prev
        else:
            head = prev
        tail.next = curr
        return head
        
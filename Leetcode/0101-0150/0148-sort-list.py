'''
Author : MiKueen
Level : Medium
Problem Statement : Sort List

Sort a linked list in O(n log n) time using constant space complexity.

Example 1:
Input: 4->2->1->3
Output: 1->2->3->4

Example 2:
Input: -1->5->3->4->0
Output: -1->0->3->4->5
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        if head is None or head.next is None:
            return head
        temp = slow = fast = head
        while fast and fast.next:
            temp = slow
            slow = slow.next
            fast = fast.next.next
        temp.next  = None
        left = self.sortList(head)
        right = self.sortList(slow)
        return self.mergeList(left, right)
    
    def mergeList(self, left, right):
        curr = head = ListNode(None)
        while left and right:
            if left.val <= right.val:
                curr.next = left
                left = left.next
                curr = curr.next
            else:
                curr.next = right
                right = right.next    
                curr = curr.next
        curr.next = left or right
        return head.next

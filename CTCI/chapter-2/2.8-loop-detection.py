'''
Author : MiKueen
Problem Statement : Loop Detection

Given a circular linked list, implement an algorithm that returns the node at the
beginning of the loop.
DEFINITION
Circular linked list: A (corrupt) linked list in which a node's next pointer points to an earlier node, so
as to make a loop in the linked list.

EXAMPLE
Input: A -> B -> C -> D -> E -> C [the same C as earlier]
Output: C 
'''

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detect_loop(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None:
            return None

        slow = head
        fast = head
        flag = False

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if fast == slow:
                flag =  True
                break

        if not flag:
            return None

        slow = head
        while fast != slow:
            fast = fast.next
            slow = slow.next

        return slow

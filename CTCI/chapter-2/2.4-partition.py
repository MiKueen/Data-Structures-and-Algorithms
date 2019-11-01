'''
Author : MiKueen
Problem Statement : Partition

Write code to partition a linked list around a value x, such that all nodes less than x come
before all nodes greater than or equal to x. If x is contained within the list the values of x only need
to be after the elements less than x (see below). The partition element x can appear anywhere in the
"right partition"; it does not need to appear between the left and right partitions.

EXAMPLE
Input: 3 -> 5 -> 8 -> 5 -> 10 -> 2 -> 1 [partition= 5]
Output: 3 -> 1 -> 2 -> 10 -> 5 -> 5 -> 8

Approach :
1) Make two list, one for storing values less than x and another for storing values more than x.
2) If the original list node's value is less than x, append it in left list.
3) If the original list node's value is greater than or equal to x, append it to right list.
4) As last node of right list is ending node, assign its next to None.
5) Combine both the lists by joining last node of left list to head of right list.
6) Return head of left lists after joining.
'''

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        left = left_head = ListNode(0)
        right = right_head = ListNode(0)

        while head:
            if head.val < x:
                left.next = head
                left = left.next
            else:
                right.next = head
                right = right.next
            head = head.next

        right.next = None
        left.next = right_head.next
        return left_head.next

'''
Author : MiKueen
Level : Hard
Problem Statement : Merge k Sorted Lists

Merge k sorted linked lists and return it as one sorted list. Analyze and describe its complexity.

Example:
Input:
[
  1->4->5,
  1->3->4,
  2->6
]
Output: 1->1->2->3->4->4->5->6
'''

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        curr = head = ListNode(0)
        while l1 and l2:
            if l1.val <= l2.val:
                curr.next = l1
                l1 = l1.next
            else:
                curr.next = l2
                l2 = l2.next
            curr = curr.next
        curr.next = l1 or l2
        return head.next
    
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        if not lists:
            return None
        i , n = 0 , len(lists)-1
            
        while i != n or n != 0:
            if i >= n:
                i = 0
            else:
                lists[i] = self.mergeTwoLists(lists[i], lists[n])
                i += 1
                n -= 1
        return lists[0]

'''
Complexity Analysis

> Time complexity : O(Nlogk) where k is the number of linked lists.
    - We can merge two sorted linked list in O(n) time where n is the total number of nodes in two lists.
    - Sum up the merge process and we can get: O(Nlogk)

> Space complexity : O(1)
    - We can merge two sorted linked lists in O(1) space.
'''

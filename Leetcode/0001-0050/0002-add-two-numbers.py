'''
Author : MiKueen
Level : Medium
Problem Statement : Add Two Numbers

You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.
You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example:
Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
Explanation: 342 + 465 = 807.
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        res = ListNode(0)
        temp = res
        carry = 0
                
        while l1 or l2 or carry:            
            val1  = l1.val if l1 else 0
            val2  = l2.val if l2 else 0
            lsum = carry + val1 + val2
  
            carry = 1 if lsum >= 10 else 0
            lsum = lsum if lsum < 10 else lsum % 10  
                      
            temp.next = ListNode(lsum)
            temp = temp.next                      
            
            l1 = (l1.next if l1 else None)
            l2 = (l2.next if l2 else None)
               
        return res.next
            
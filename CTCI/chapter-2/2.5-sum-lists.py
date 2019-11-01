'''
Author : MiKueen
Problem Statement : Sum Lists

You have two numbers represented by a linked list, where each node contains a single
digit. The digits are stored in reverse order, such that the 1 's digit is at the head of the list. Write a
function that adds the two numbers and returns the sum as a linked list.

EXAMPLE
Input: (7-> 1 -> 6) + (5 -> 9 -> 2).That is,617 + 295.
Output: 2 -> 1 -> 9. That is, 912.

FOLLOW UP
Suppose the digits are stored in forward order. Repeat the above problem.
Input: (6 -> 1 -> 7) + (2 -> 9 -> 5).That is,617 + 295.
Output: 9 -> 1 -> 2. That is, 912. 
'''

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def sum_lists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
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


    # FOLLOW UP 
    def sum_lists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        num1, num2 = 0, 0
        while l1 or l2:
            if l1: 
                num1 = num1*10 + l1.val
                l1 = l1.next
            if l2:
                num2 = num2*10 + l2.val
                l2 = l2.next
                
        res = str(num1 + num2)
        if int(res) == 0:
            return ListNode(res)
        
        head = ListNode(None)
        curr = head
        for i in str(res):
            curr.next = ListNode(int(i))
            curr = curr.next

        return head.next

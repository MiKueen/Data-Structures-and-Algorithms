'''
Author : MiKueen
Level : Easy
Problem Statement : Palindrome Linked Lists

Given a singly linked list, determine if it is a palindrome.

Example 1:
Input: 1->2
Output: false

Example 2:
Input: 1->2->2->1
Output: true
Follow up:
Could you do it in O(n) time and O(1) space?
'''

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if head is None or head.next is None:
            return True

        slow = fast = head

        '''
        # Method 1
        # Using stack, O(n) Space Complexity

        stack = []
        while slow:
            stack.append(slow.val)
            slow = slow.next

        while fast:
            if fast.val != stack.pop():
                return False
            fast = fast.next

        return True
        '''

        # Method 2
        # Reversing second half of list, O(1) Space Complexity

        prev_node = None
        while fast and fast.next:       
            fast = fast.next.next
            head = head.next
        
           # reverse first half
            next_node = slow.next
            slow.next = prev_node
            prev_node = slow
            slow = next_node
            
        if fast:
            head = head.next
        
        # compare the (first reversed half) and the (second half)    
        while prev_node and head:
            if prev_node.val!=head.val:
                return False
            
            prev_node = prev_node.next
            head = head.next
        
        return True

'''
Author : MiKueen
Problem Statement : Return Kth to Last

Implement an algorithm to find the kth to last element of a singly linked list. 
'''

# Using two pointer method

def return_kth_to_last(head, k):
    if head is None:
        return None
    
    slow = fast = head
    for i in range(k):
        fast = fast.next
    
    while fast: 
        fast = fast.next 
        slow = slow.next    
    
    return slow

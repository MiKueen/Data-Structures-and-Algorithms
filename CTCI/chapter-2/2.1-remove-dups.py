'''
Author : MiKueen
Problem Statement : Remove Dups

Write code to remove duplicates from an unsorted linked list.

FOLLOW UP
How would you solve this problem if a temporary buffer is not allowed? 
'''

# Method 1
# O(n) Time Complexity using buffer
def remove_dups(head):
    if head is None:
        return 

    curr = head
    mapping = {}
    mapping[curr.val] = True

    while curr.next:
        if curr.next.val not in mapping:
            mapping[curr.next.val] = True
            curr = curr.next
        else:
            curr.next = curr.next.next

    return head


# Method 2
# O(n^2) Time Complexity without using extra buffer
def remove_dups(head):
    if head is None:
        return 

    curr = head
    while curr:
        node = curr
        while node.next:
            if node.next.val == curr.val:
                node.next = node.next.next
            else:
                node = node.next
        curr = curr.next

    return head

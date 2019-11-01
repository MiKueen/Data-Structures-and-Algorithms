'''
Author : MiKueen
Problem Statement : Palindrome

Implement a function to check if a linked list is a palindrome. 
'''

# Method 1
# Using stack, O(n) Space Complexity
def palindrome(head):
    if head is None or head.next is None:
    	return True

    stack = []
    slow = fast = head

    while slow:
    	stack.append(slow.val)
    	slow = slow.next

    while fast:
    	if fast.val != stack.pop():
    		return False
    	fast = fast.next

    return True


# Method 2
# Reversing second half of list, O(1) Space Complexity
def palindrome(head):
	if head is None or head.next is None:
            return True

        slow = fast = head
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

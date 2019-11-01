'''
Author : MiKueen
Problem Statement : Delete Middle Node

Implement an algorithm to delete a node in the middle (i.e., any node but
the first and last node, not necessarily the exact middle) of a singly linked list, given only access to
that node.

EXAMPLE
Input: the node c from the linked list a->b->c->d->e->f
Result: nothing is returned, but the new linked list looks like a ->b->d->e->f 
'''

def delete_node(node):
    if node == None:
        pass
    else:
        next_node = node.next
        node.val = next_node.val
        node.next = next_node.next

# NOTE :  This problem cannot be solved if the node to be deleted is the last node in the linked list. 
    
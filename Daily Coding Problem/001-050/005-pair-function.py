'''
Author : MiKueen
Level : Medium
Company : Jane Street
Problem Statement : Pair function

cons(a, b) constructs a pair, and car(pair) and cdr(pair) returns the first and last element of that pair. 
For example, car(cons(3, 4)) returns 3, and cdr(cons(3, 4)) returns 4.

Given this implementation of cons:

def cons(a, b):
    def pair(f):
        return f(a, b)
    return pair

Implement car and cdr.
'''

def cons(a, b):
    def pair(f):
        return f(a, b)
    return pair

def car(f):
    """
    :type f: function
    :rtype: int
    """
    def first(a, b):
        return a
    return f(first)

def cdr(f):
    """
    :type f: function
    :rtype: int
    """
    def last(a, b):
        return b
    return f(last)

assert car(cons(3, 4)) == 3
assert cdr(cons(3, 4)) == 4

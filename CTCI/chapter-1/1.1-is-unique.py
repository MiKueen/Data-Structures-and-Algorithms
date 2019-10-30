'''
Author : MiKueen
Problem Statement : Is Unique

Implement an algorithm to determine if a string has all unique characters. 
What if you cannot use additional data structures?
'''

# Method 1
# Without using extra data structure
def is_unique(s):
    s.sort() 
    for i in range(len(s)-1):
        if s[i] == s[i+1]:
            return False
    return True

# Method 2
# Using extra data structure
def is_unique(s):
    mapping = {}
    for char in s:
        if char in mapping:
            return False
        mapping[char] = True
    return True

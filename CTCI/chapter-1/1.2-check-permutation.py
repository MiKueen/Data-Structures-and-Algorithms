'''
Author : MiKueen
Problem Statement : Check Permutation

Given two strings, write a method to decide if one is a permutation of the
other. 
'''

from collections import Counter as cnt

# Method 1 
# Using Counter
def check_permute(str1, str2):
    return cnt(str1) == cnt(str2)

# Method 2
# By sorting (anagram check)
def check_permute(str1, str2):
    if len(str1) != len(str2):
        return False
    str1 = "".join(sorted(str1))
    str2 = "".join(sorted(str2))
    return str1 == str2

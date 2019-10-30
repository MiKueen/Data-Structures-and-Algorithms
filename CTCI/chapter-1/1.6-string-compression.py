'''
Author : MiKueen
Problem Statement : String Compression

Implement a method to perform basic string compression using the counts
of repeated characters. For example, the string aabcccccaaa would become a2blc5a3. If the
"compressed" string would not become smaller than the original string, your method should return
the original string. You can assume the string has only uppercase and lowercase letters (a - z). 
'''

# Using Ordered Dictionary

from collections import OrderedDict as dict

def compression(s):
    s = s.lower()
    mapping = dict.fromkeys(s, 0)
    res = ''
    for char in s:
        mapping[char] += 1
    for char, cnt in mapping.items():
        if cnt == 1:
            res += char
        else:
            res += cnt + str(cnt)
    return ans

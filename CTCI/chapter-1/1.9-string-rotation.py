'''
Author : MiKueen
Problem Statement : String Rotation

Assume you have a method isSubstringwhich checks if oneword is a substring
of another. Given two strings, sl and s2, write code to check if s2 is a rotation of sl using only one
call to isSubstring (e.g., "waterbottle" is a rotation of"erbottlewat"). 
'''

def string_rotation(str1, str2):
    if len(str1) != len(str2):
        return False
    res = str1 + str1
    if str2 in res:
        return True
    return False

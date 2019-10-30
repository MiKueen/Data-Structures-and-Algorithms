'''
Author : MiKueen
Problem Statement : Palindrome Permutation

Given a string, write a function to check if it is a permutation of a palindrome. A palindrome is a word or phrase that is the same forwards and backwards. A permutation
is a rearrangement of letters. The palindrome does not need to be limited to just dictionary words.

EXAMPLE
Input: Tact Coa
Output: True (permutations: "taco cat", "atco cta", etc.) 
'''

def palindrome_permute(s):
    s = s.lower(s.replace(" ",""))
    mapping, temp = {}, 0

    for char in s:
    	if char not in mapping:
    		mapping[char] = 1
    	else:
    		mapping[char] += 1

    for char, cnt in mapping.items():
    	if cnt % 2 != 0:
    		temp += 1
    	if temp > 1:
    		return False

    return True

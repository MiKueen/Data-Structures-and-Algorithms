'''
Author : MiKueen
Problem Statement : URLify

Write a method to replace all spaces in a string with '%20'. You may assume that the string
has sufficient space at the end to hold the additional characters, and that you are given the "true"
length of the string.

EXAMPLE
Input: "Mr John Smith ", 13
Output: "Mr%20John%20Smith" 
'''

# Method 1
# Pythonic way
def urlify(s):
	return s.strip().replace(" ", "%20")

# Method 2
def urlify(s):
	new_len = len(s)

	for i in range(len(s)):
		if s[i] == ' ':
    		s.append(' ')
    		s.append(' ')
    		new_len += 2

    for i in range(len(s)-1, -1, -1):
    	if s[i] == ' ':
    		s[new_len-1] = '0'
    		s[new_len-2] = '2'
    		s[new_len-3] = '%'
    		new_len -= 3
    	else:
    		s[new_len-1] = s[i]
    		new_len -= 1

    return s

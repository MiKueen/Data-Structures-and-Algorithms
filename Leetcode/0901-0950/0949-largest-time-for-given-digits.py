'''
Author : MiKueen
Level : Easy
Problem Statement : Largest Time for Given Digits

Given an array of 4 digits, return the largest 24 hour time that can be made.
The smallest 24 hour time is 00:00, and the largest is 23:59.  Starting from 00:00, a time is larger if more time has elapsed since midnight.
Return the answer as a string of length 5.  If no valid time can be made, return an empty string.

Example 1:
Input: [1,2,3,4]
Output: "23:41"

Example 2:
Input: [5,5,5,5]
Output: ""
 
Note:
A.length == 4
0 <= A[i] <= 9
'''

class Solution:
    def largestTimeFromDigits(self, A: List[int]) -> str:
        if min(A) > 2:
            return ""
    
        time = itertools.permutations(sorted(A, reverse=True))
        for t in time:
            if t[:2] < (2, 4) and t[2] < 6:
                return f"{t[0]}{t[1]}:{t[2]}{t[3]}"
                
        return ""

'''
Author : MiKueen
Level : Medium
Problem Statement : Implement Rand10() using Rand7()

Given a function rand7 which generates a uniform random integer in the range 1 to 7, write a function rand10 which generates a uniform random integer in the range 1 to 10.
Do NOT use system's Math.random().

Example 1:
Input: 1
Output: [7]

Example 2:
Input: 2
Output: [8,4]

Example 3:
Input: 3
Output: [8,1,10]
 
Note:
rand7 is predefined.
Each testcase has one argument: n, the number of times that rand10 is called.
 
Follow up:
What is the expected value for the number of calls to rand7() function?
Could you minimize the number of calls to rand7()?
'''

# The rand7() API is already defined for you.
# def rand7():
# @return a random integer in the range 1 to 7

class Solution:
    def rand10(self):
        """
        :rtype: int
        """
        rand40 = 40
        while rand40 >= 40:
            rand40 = (rand7() - 1) * 7 + rand7() - 1
        return rand40 % 10 + 1
    
'''
# The randN() API is already defined for you.
# def randN():
# @return a random integer in the range 1 to N

class Solution:

    # Generalised solution for creating randM() if randN() is given
    def randM(self, N, M):
        """
        :rtype: int
        """

        # acceptable is the desired range which can generate required integer directly
        curr = acceptable = N * N - (N * N) % M 

        # if current no is not in the acceptable range, discard it and repeat the process again
        while curr >= acceptable:
            curr = (randN() - 1) * N + randN() - 1
        return curr % M + 1
'''

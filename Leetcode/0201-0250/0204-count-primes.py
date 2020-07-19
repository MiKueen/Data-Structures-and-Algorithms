'''
Author : MiKueen
Level : Easy
Problem Statement : Count Primes

Count the number of prime numbers less than a non-negative number, n.

Example:
Input: 10
Output: 4
Explanation: There are 4 prime numbers less than 10, they are 2, 3, 5, 7.
'''

class Solution:
    def countPrimes(self, n: int) -> int:
        if n <= 2:
            return 0
        # Using Seive of Eratosthenes
        primes = [True]*(n)
        primes[0] = primes[1] = False
        for i in range(2, int(n**0.5) + 1):
            if primes[i] == True:
                for j in range(i * i, n, i):
                    primes[j] = False        
        cnt = 0
        for i in range(len(primes)):
            if primes[i] == True:
                cnt += 1
        return cnt
        
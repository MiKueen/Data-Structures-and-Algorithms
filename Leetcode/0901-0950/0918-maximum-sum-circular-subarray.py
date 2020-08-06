'''
Author : MiKueen
Level : Medium
Problem Statement : Maximum Sum Circular Subarray

Given a circular array C of integers represented by A, find the maximum possible sum of a non-empty subarray of C.
Here, a circular array means the end of the array connects to the beginning of the array.  (Formally, C[i] = A[i] when 0 <= i < A.length, and C[i+A.length] = C[i] when i >= 0.)
Also, a subarray may only include each element of the fixed buffer A at most once.  (Formally, for a subarray C[i], C[i+1], ..., C[j], there does not exist i <= k1, k2 <= j with k1 % A.length = k2 % A.length.)

Example 1:
Input: [1,-2,3,-2]
Output: 3
Explanation: Subarray [3] has maximum sum 3

Example 2:
Input: [5,-3,5]
Output: 10
Explanation: Subarray [5,5] has maximum sum 5 + 5 = 10

Example 3:
Input: [3,-1,2,-1]
Output: 4
Explanation: Subarray [2,-1,3] has maximum sum 2 + (-1) + 3 = 4

Example 4:
Input: [3,-2,2,-3]
Output: 3
Explanation: Subarray [3] and [3,-2,2] both have maximum sum 3

Example 5:
Input: [-2,-3,-1]
Output: -1
Explanation: Subarray [-1] has maximum sum -1

Note:
-30000 <= A[i] <= 30000
1 <= A.length <= 30000
'''

class Solution:
    def maxSubarraySumCircular(self, A: List[int]) -> int:
    
        if max(A) <= 0:
            return max(A)

        # Method 1 : Kadane's Algorithm
        max_sum = curr_max = min_sum = curr_min = A[0] 
        
        for i in range(1, len(A)): 
            curr_max = max(A[i], curr_max + A[i]) 
            max_sum = max(max_sum, curr_max)
            curr_min = min(A[i], curr_min + A[i]) 
            min_sum = min(min_sum, curr_min)
            
        return max(max_sum, sum(A) - min_sum)
            
        
        # Method 2 : Dynamic Programming
        max_dp = [i for i in A]
        min_dp = [i for i in A]
        
        for i in range(1,len(A)):
            if max_dp[i-1] > 0:
                max_dp[i] += max_dp[i-1]
            if min_dp[i-1] < 0:
                min_dp[i] += min_dp[i-1]

        return max(max(max_dp), sum(A) - min(min_dp))
                       
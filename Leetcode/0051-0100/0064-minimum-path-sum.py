'''
Author : MiKueen
Level : Medium
Problem Statement :Minimum Path Sum

Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right which minimizes the sum of all numbers along its path.
Note: You can only move either down or right at any point in time.

Example:
Input:
[
  [1,3,1],
  [1,5,1],
  [4,2,1]
]
Output: 7
Explanation: Because the path 1→3→1→1→1 minimizes the sum.
'''

class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if not grid:
            return 
        m, n = len(grid), len(grid[0])
        
        # Dp In Place Solution
        for j in range(1, n):
            grid[0][j] += grid[0][j-1]
        for i in range(1, m):
            grid[i][0] += grid[i-1][0]
            
        for i in range(1, m):
            for j in range(1, n):
                grid[i][j] += min(grid[i-1][j], grid[i][j-1])
                
        return grid[m-1][n-1]

        '''
        # O(m*n) Space Complexity
        dp = [[0] * n for i in range(m)]
        dp[0][0] = grid[0][0]
        
        for j in range(1,n):
            dp[0][j] = grid[0][j] + dp[0][j-1]
            
        for i in range(1,m):
            dp[i][0] = grid[i][0] + dp[i-1][0]
            
        for i in range(1,m):
            for j in range(1,n):
                dp[i][j] = grid[i][j] + min(dp[i-1][j],dp[i][j-1])  
                
        return dp[m-1][n-1]
        '''     
                                       
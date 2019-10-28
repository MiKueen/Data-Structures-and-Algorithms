'''
Author : MiKueen
Level : Medium
Problem Statement : Triangle

Given a triangle, find the minimum path sum from top to bottom. Each step you may move to adjacent numbers on the row below.
For example, given the following triangle
[
     [2],
    [3,4],
   [6,5,7],
  [4,1,8,3]
]
The minimum path sum from top to bottom is 11 (i.e., 2 + 3 + 5 + 1 = 11).
Note:
Bonus point if you are able to do this using only O(n) extra space, where n is the total number of rows in the triangle.
'''

class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        if not triangle:
            return
         
        # DP in place bottom-up solution
        # start with second last row and use last row to form dp table
        for i in range(len(triangle)-2, -1, -1):
            for j in range(len(triangle[i])):
                
                # find minimum adjacent element from next row and sum it with current element
                triangle[i][j] += min(triangle[i+1][j], triangle[i+1][j+1])
                
        return triangle[0][0]
        
        
        '''
        # DP in place top-down solution  
        for i in range(1, len(triangle)):
            for j in range(len(triangle[i])):
                
                # sum 1st element of current row with 1st element of previous row
                if j == 0:
                    triangle[i][j] += triangle[i-1][j]
                    
                # check last element of current row with last element of previous row
                elif j == len(triangle[i])-1:
                    triangle[i][j] += triangle[i-1][j-1]
                    
                # check adjacent elements from previous row and sum with current element
                else:
                    triangle[i][j] += min(triangle[i-1][j-1], triangle[i-1][j])
                    
        return min(triangle[-1])
        '''
       
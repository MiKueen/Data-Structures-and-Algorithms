'''
Author : MiKueen
Level : Easy
Problem Statement : Pascal's Triangle

Given a non-negative integer numRows, generate the first numRows of Pascal's triangle.
In Pascal's triangle, each number is the sum of the two numbers directly above it.

Example:
Input: 5
Output:
[
     [1],
    [1,1],
   [1,2,1],
  [1,3,3,1],
 [1,4,6,4,1]
]
'''

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 0:
            return []
        elif numRows == 1:
            return  [[1]]
        elif numRows == 2:
            return [[1],[1,1]]
        else:
            res = [[1],[1,1]]
            for i in range(2, numRows):
                row = [1] + [0]*(i-1) + [1]
                for j in range(1,i):
                    row[j] = res[i-1][j-1] + res[i-1][j]
                res.append(row)
            return res
            
'''
Author : MiKueen
Level : Medium
Problem Statement : Spiral Matrix

Given a matrix of m x n elements (m rows, n 
return all elements of the matrix in spiral order.

Example 1:
Input:
[
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]
Output: [1,2,3,6,9,8,7,4,5]

Example 2:
Input:
[
  [1, 2, 3, 4],
  [5, 6, 7, 8],
  [9,10,11,12]
]
Output: [1,2,3,4,8,12,11,10,9,5,6,7]
'''

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if len(matrix) == 0:
            return []
        rows, cols = len(matrix)-1, len(matrix[0])-1
        top, down, left, right = 0, rows, 0, cols
        d, res = 0, []
        while top <= down and left <= right:
            if d == 0:
                for i in range(left, right+1):
                    res.append(matrix[top][i])
                top += 1
            elif d == 1:
                for i in range(top, down+1):
                    res.append(matrix[i][right])
                right -= 1
            elif d == 2:
                for i in range(right, left-1, -1):
                    res.append(matrix[down][i])
                down -= 1
            elif d == 3:
                for i in range(down, top-1, -1):
                    res.append(matrix[i][left])
                left += 1
            d = (d+1) % 4
        return res
    
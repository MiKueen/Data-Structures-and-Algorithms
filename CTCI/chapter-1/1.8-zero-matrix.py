'''
Author : MiKueen
Problem Statement : Zero Matrix

Write an algorithm such that if an element in an MxN matrix is 0, its entire row and
column are set to 0. 
'''

def zero_matrix(matrix):
    flag = True
    m, n = len(matrix), len(matrix[0])

    for i in range(m):
        if matrix[i][0] == 0:
            flag = False
        for j in range(1, n):
            if matrix[i][j] == 0:
                matrix[i][0] = matrix[0][j] = 0

    for i in range(m-1, -1, -1):
        for j in range(1, n):
            if matrix[i][0] == 0 or matrix[0][j] == 0:
                matrix[i][j] = 0
        if not flag:
            matrix[i][0] = 0

    for i in range(m):
        print(matrix[i])
        
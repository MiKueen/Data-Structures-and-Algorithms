'''
Author : MiKueen
Problem Statement : Rotate Matrix

Given an image represented by an NxN matrix, where each pixel in the image is
4 bytes, write a method to rotate the image by 90 degrees. Can you do this in
place?
'''

def rotate_matrix(image):
    n = len(image)
    
    for i in range(n//2):
        for j in range(i,n-i-1):
            temp                = image[i][j]
            image[i][j]         = image[n-j-1][i]
            image[n-j-1][i]     = image[n-i-1][n-j-1]
            image[n-i-1][n-j-1] = image[j][n-i-1]
            image[j][n-i-1]     = temp
    
    for i in range(n):
        print(image[i])

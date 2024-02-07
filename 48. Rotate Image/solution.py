"""
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        Do not return anything, modify matrix in-place instead.
"""

def rotate(matrix):
     # Time Complexity: O(n^2)
     # Space Complexity: O(1)
     
     n = len(matrix)

     # transpose the matrix
     for i in range(n):
          for j in range(i+1, n):
               matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

     # reverse each row
     for i in range(n):
          matrix[i] = matrix[i][::-1]

     return matrix
     
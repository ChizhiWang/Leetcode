"""
 Minimum Falling Path Sum

 Given an n x n array of integers matrix, return the minimum sum of any falling path through matrix.

A falling path starts at any element in the first row and chooses the element in the next row that is either directly below or diagonally left/right. Specifically, the next element from position (row, col) will be (row + 1, col - 1), (row + 1, col), or (row + 1, col + 1).
"""

class Solution:
    def minFallingPathSum(self, matrix: list[list[int]]) -> int:
        m, n = len(matrix), len(matrix[0])
        for i in range(1, m):
            for j in range(n):
                minabove = matrix[i-1][j]
                if j > 0:
                    minabove = min(minabove, matrix[i-1][j-1])
                if j < n-1:
                    minabove = min(minabove, matrix[i-1][j+1])
                matrix[i][j] += minabove
        return min(matrix[m-1])
    
matrix = [[2,1,3],[6,5,4],[7,8,9]]
print(Solution.minFallingPathSum(Solution, matrix))

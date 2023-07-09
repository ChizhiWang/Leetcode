"""
Maximal Square

Given an m x n binary matrix filled with 0's and 1's, find the largest square containing only 1's and return its area.
"""

class Solution:
    def maximalSquare(self, matrix: list[list[str]]) -> int:
        m, n = len(matrix), len(matrix[0])
        square = [[0 for j in range(n)] for i in range(m)]
        r = 0
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == '1':
                    if i == 0 or j == 0:
                        square[i][j] = 1
                    else:
                        square[i][j] = min(square[i-1][j], square[i][j-1], square[i-1][j-1]) + 1
                    r = max(r, square[i][j])
        return r*r
    

matrix = matrix = [["0","1"],["1","0"]]
print(Solution.maximalSquare(Solution, matrix))
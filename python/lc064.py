"""
Minimum Path Sum

Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right, which minimizes the sum of all numbers along its path.

Note: You can only move either down or right at any point in time.
"""

class Solution:
    def minPathSum(self, grid: list[list[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        dp = [[0 for j in range(n)] for i in range(m)]
        dp[0][0] = grid[0][0]
        for j in range(1, n):
            dp[0][j] = grid[0][j] + dp[0][j-1]
        for i in range(1, m):
            dp[i][0] = grid[i][0] + dp[i-1][0]
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + grid[i][j]
        return dp[m-1][n-1]


grid = [[7,4,8,7,9,3,7,5,0],[1,8,2,2,7,1,4,5,7],[4,6,4,7,7,4,8,2,1],[1,9,6,9,8,2,9,7,2],[5,5,7,5,8,7,9,1,4],[0,7,9,9,1,5,3,9,4]]
print(Solution.minPathSum(Solution, grid))
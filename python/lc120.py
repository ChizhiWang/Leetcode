"""
Triangle

Given a triangle array, return the minimum path sum from top to bottom.

For each step, you may move to an adjacent number of the row below. More formally, if you are on index i on the current row, you may move to either index i or index i + 1 on the next row.
"""

class Solution:
    def minimumTotal(self, triangle: list[list[int]]) -> int:
        m = len(triangle)
        for i in range(1, m):
            triangle[i][0] += triangle[i-1][0]
            triangle[i][i] += triangle[i-1][i-1]
        for i in range(1, m):
            for j in range(1, i):
                triangle[i][j] += min(triangle[i-1][j-1], triangle[i-1][j])
        return min(triangle[m-1])

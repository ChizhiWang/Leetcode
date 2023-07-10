"""
Longest Palindromic Subsequence

Given a string s, find the longest palindromic subsequence's length in s.

A subsequence is a sequence that can be derived from another sequence by deleting some or no elements without changing the order of the remaining elements.
"""

from functools import cache


class Solution:
    def longestPalindromeSubseq1(self, s: str) -> int:
        """
        If the first and last characters are the same, both characters are guaranteed to be considered in the final palindrome. As a result, we add 2 to our answer variable and recursively remove the first and last characters from the remaining substring.

If the first and last characters aren’t the same, they cannot both occur in the final palindrome. As a result, we recurse over the substring removing the first and also recurse over the substring removing the last character. As we want the longest palindromic subsequence, we pick the maximum out of both of these.

To perform this recursion, we use two pointers, i and j, where i is the index of the first character and j is the index of the last character, to form a substring of s that is being considered. As a result, the recursive relation can be written as follows:

If s[i] == s[j], perform answer = 2 + LPS(i + 1, j - 1).
Else, perform answer = max(LPS(i, j - 1), LPS(i + 1, j).
        """
        n = len(s)
        
        memo = {}
        def lps(l, r):
            if (l,r) in memo:
                return memo[(l,r)]
            if l > r:
                return 0
            if l == r:
                return 1

            if s[l] == s[r]:
                memo[(l,r)] = lps(l + 1, r - 1) + 2
            else:
                memo[(l,r)] = max(lps(l, r - 1), lps(l + 1, r))
            return memo[(l, r)]

        return lps(0, n - 1)
    
    def longestPalindromeSubseq2(self, s: str) -> int:
        """
        we create a 2D-array dp, where dp[i][j] contains the answer of the longest palindromic subsequence of the substring formed from index i to j in s. Our answer would be dp[0][n - 1], where n is the size of s. The state transition would be as follows:

    If s[i] == s[j], perform dp[i][j] = 2 + dp[i + 1][j - 1].
    Otherwise, perform dp[i][j] = max(dp[i][j - 1], dp[i + 1][j].
        """
        n = len(s)
        dp = [[0] * n for _ in range(n)]

        for i in range(n - 1, -1, -1):
            dp[i][i] = 1
            for j in range(i + 1, n):
                if s[i] == s[j]:
                    dp[i][j] = dp[i + 1][j - 1] + 2
                else:
                    dp[i][j] = max(dp[i + 1][j], dp[i][j - 1])

        return dp[0][n - 1]


s = 'bbbab'
            
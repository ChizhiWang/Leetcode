"""
House Robber

You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security systems connected and it will automatically contact the police if two adjacent houses were broken into on the same night.

Given an integer array nums representing the amount of money of each house, return the maximum amount of money you can rob tonight without alerting the police.
"""

class Solution:
    def rob(self, nums: list[int]) -> int:
        n = len(nums)
        if n == 0:
            return 0
        elif n == 1:
            return nums[0]
        dp = [0]*(n+1)
        dp[1] = nums[0]
        for i in range(2, n+1):
            # rob the last one
            sum1 = nums[i-1] + dp[i-2]
            # not rob the last one
            sum2 = dp[i-1]
            dp[i] = max(sum1, sum2)
        return dp[n]

ans = Solution.rob(Solution, [1, 2, 3, 1])
print(ans)
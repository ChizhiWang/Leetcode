"""
Delete and Earn

You are given an integer array nums. You want to maximize the number of points you get by performing the following operation any number of times:

Pick any nums[i] and delete it to earn nums[i] points. Afterwards, you must delete every element equal to nums[i] - 1 and every element equal to nums[i] + 1.
Return the maximum number of points you can earn by applying the above operation some number of times.


"""

from collections import defaultdict
from functools import cache


class Solution:
    def deleteAndEarn1(self, nums: list[int]) -> int:
        # top-down: from what we want to base case
        # generate the dict of numbers
        points = defaultdict(int)
        max_number = 0
        for num in nums:
            points[num] += num
            max_number = max(max_number, num)

        # @cache
        def max_point(n):
            if n == 0:
                return 0
            elif n == 1:
                return points[1]
        
            # not delete the last one
            sum1 = max_point(n-1)
            # delete the last one
            sum2 = max_point(n-2) + points[n]
            return max(sum1, sum2)
        
        return max_point(max_number)
    
    def deleteAndEarn2(self, nums: list[int]) -> int:
        # bottom-up: from the base case to what we want
        # generate the dict of numbers
        points = defaultdict(int)
        max_number = 0
        for num in nums:
            points[num] += num
            max_number = max(max_number, num)
        
        max_points = [0]*(max_number+1)
        max_points[1] = points[1]

        for n in range(2, len(max_points)):
            max_points[n] = max(max_points[n-1], max_points[n-2]+points[n])

        return max_points[max_number]
        


    
print(Solution.deleteAndEarn1(Solution, [2,2,3,3,3,4]))


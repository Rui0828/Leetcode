#
# @lc app=leetcode id=368 lang=python3
#
# [368] Largest Divisible Subset
#
from typing import List
# @lc code=start
class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        nums = sorted(nums)
        dp  = [[n] for n in nums]

        for i in range(len(nums)):
            for j in range(i):
                if nums[i] % nums[j] == 0 and len(dp[j])+1 > len(dp[i]):
                    dp[i] = dp[j].copy()
                    dp[i].append(nums[i])
        
        return max(dp, key=len)
# @lc code=end


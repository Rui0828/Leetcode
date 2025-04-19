#
# @lc app=leetcode id=2563 lang=python3
#
# [2563] Count the Number of Fair Pairs
#
import math
# @lc code=start
class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        nums = sorted(nums)

        s, e = 0, len(nums)-1
        u_cnt = 0
        while s < e:
            if nums[s]+nums[e] > upper:
                u_cnt += (e-s)
                e -= 1
            else:
                s += 1
        

        s, e = 0, len(nums)-1
        d_cnt = 0
        while s < e:
            if nums[s]+nums[e] < lower:
                d_cnt += (e-s)
                s += 1
            else:
                e -=1

        return math.comb(len(nums), 2) - u_cnt - d_cnt
# @lc code=end


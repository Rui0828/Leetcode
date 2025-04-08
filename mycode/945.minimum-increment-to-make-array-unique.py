#
# @lc app=leetcode id=945 lang=python3
#
# [945] Minimum Increment to Make Array Unique
#
from typing import List
# @lc code=start
class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        
        nums = sorted(nums)

        cnt = 0
        for i in range(1, len(nums)):
            if nums[i] <= nums[i-1]:
                dif = nums[i-1] - nums[i] + 1
                nums[i] += dif
                cnt += dif
        
        return cnt
        
# @lc code=end


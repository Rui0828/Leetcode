#
# @lc app=leetcode id=3392 lang=python3
#
# [3392] Count Subarrays of Length Three With a Condition
#
from typing import List
# @lc code=start
class Solution:
    def countSubarrays(self, nums: List[int]) -> int:
        cnt = 0

        for i in range(len(nums)-2):
            if (nums[i]+nums[i+2])*2==nums[i+1]:
                cnt += 1
        
        return cnt
# @lc code=end


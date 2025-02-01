#
# @lc app=leetcode id=3151 lang=python3
#
# [3151] Special Array I
#
from typing import List
# @lc code=start
class Solution:
    def isArraySpecial(self, nums: List[int]) -> bool:
        if len(nums) == 1:
            return True
        else:
            tmp = nums[0]%2
            for i in range(1, len(nums)-1):
                new = nums[i]%2
                if  new == tmp:
                    return False
                tmp = new
            
            return True
# @lc code=end


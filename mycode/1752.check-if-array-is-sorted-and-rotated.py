#
# @lc app=leetcode id=1752 lang=python3
#
# [1752] Check if Array Is Sorted and Rotated
#
from typing import List

# @lc code=start
class Solution:
    def check(self, nums: List[int]) -> bool:
        
        rot = True
        
        for i in range(len(nums)):
            if i != len(nums) -1:
                if nums[i] > nums[i+1]:
                    if rot:
                        rot = False
                    else:
                        return False
            else:
                if nums[i] > nums[0]:
                    if rot:
                        rot = False
                    else:
                        return False
        
        return True
# @lc code=end


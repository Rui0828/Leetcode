#
# @lc app=leetcode id=283 lang=python3
#
# [283] Move Zeroes
#

# @lc code=start
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        f = 0
        for i in range(n):
            if nums[i] != 0:
                nums[f] = nums[i]
                f += 1
        
        while f < n:
            nums[f] = 0
            f += 1
                 
# @lc code=end


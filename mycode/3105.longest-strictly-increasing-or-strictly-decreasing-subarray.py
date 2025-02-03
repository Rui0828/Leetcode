#
# @lc app=leetcode id=3105 lang=python3
#
# [3105] Longest Strictly Increasing or Strictly Decreasing Subarray
#

# @lc code=start
class Solution(object):
    def longestMonotonicSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ans = 1
        inc = 1
        dec = 1
        for i in range(len(nums)-1):
            if nums[i]>nums[i+1]:
                inc += 1
                dec = 1
                ans = max(ans, inc)
            elif nums[i]<nums[i+1]:
                inc = 1
                dec += 1
                ans = max(ans, dec)
            else:
                inc = 1
                dec = 1
        return ans
# @lc code=end


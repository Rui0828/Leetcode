#
# @lc app=leetcode id=1800 lang=python
#
# [1800] Maximum Ascending Subarray Sum
#

# @lc code=start
class Solution(object):
    def maxAscendingSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ans = 0
        cnt = nums[0]
        for i in range(1, len(nums)):
            if nums[i] > nums[i-1]:
                cnt += nums[i]
            else:
                ans = max(ans, cnt)
                cnt = nums[i]
        ans = max(ans, cnt)
        return ans
# @lc code=end

print(Solution().maxAscendingSum([10,20,30,5,10,50]))


#
# @lc app=leetcode id=724 lang=python3
#
# [724] Find Pivot Index
#

# @lc code=start
class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        lsum = 0
        rsum = sum(nums[1:])
        
        if rsum == 0:
            return 0

        for i in range(1, len(nums)):
            lsum += nums[i-1]
            rsum -= nums[i]

            if lsum==rsum:
                return i
        
        return -1

        
# @lc code=end


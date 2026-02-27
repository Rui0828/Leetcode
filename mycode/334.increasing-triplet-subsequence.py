#
# @lc app=leetcode id=334 lang=python3
#
# [334] Increasing Triplet Subsequence
#

# @lc code=start
class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        first = second = 2**31-1

        for i in nums:
            if i <= first:
                first = i
            elif i <= second:
                second = i
            else:
                return True

        return False
        
# @lc code=end


#
# @lc app=leetcode id=1980 lang=python3
#
# [1980] Find Unique Binary String
#

# @lc code=start
class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        for i in range(2**len(nums)):
            b = bin(i)[2:].zfill(len(nums))
            if b not in nums:
                return b
# @lc code=end


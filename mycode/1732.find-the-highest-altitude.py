#
# @lc app=leetcode id=1732 lang=python3
#
# [1732] Find the Highest Altitude
#

# @lc code=start
class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        max_h = 0
        c_h = 0
        for i in gain:
            c_h += i
            max_h = max(max_h, c_h)
        return max_h
        
# @lc code=end


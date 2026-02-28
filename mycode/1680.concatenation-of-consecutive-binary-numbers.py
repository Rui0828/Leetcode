#
# @lc app=leetcode id=1680 lang=python3
#
# [1680] Concatenation of Consecutive Binary Numbers
#

# @lc code=start
class Solution:
    def concatenatedBinary(self, n: int) -> int:
        b = ""
        for i in range(1, n+1):
            b += bin(i)[2:]
        
        return int(b, 2) % (10**9+7)
        
# @lc code=end


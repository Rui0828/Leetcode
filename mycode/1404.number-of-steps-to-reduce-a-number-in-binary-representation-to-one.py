#
# @lc app=leetcode id=1404 lang=python3
#
# [1404] Number of Steps to Reduce a Number in Binary Representation to One
#

# @lc code=start
class Solution:
    def numSteps(self, s: str) -> int:
        
        s = int(s, 2)
        cnt = 0

        while s != 1:
            if s & 1:
                cnt += 1
                s = s + 1
            cnt += 1
            s = s >> 1
        
        return cnt
            
        
# @lc code=end


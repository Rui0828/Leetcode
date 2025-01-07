#
# @lc app=leetcode id=70 lang=python
#
# [70] Climbing Stairs
#

# @lc code=start
class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        
        pre1 = 1
        pre2 = 2
        
        if n == 1:
            return 1
        if n == 2:
            return 2
        else:
            ans = 0
            for i in range(n-2):
                ans = pre1 + pre2
                pre1 = pre2
                pre2 = ans
        return ans
# @lc code=end



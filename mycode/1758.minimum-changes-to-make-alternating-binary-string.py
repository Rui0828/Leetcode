#
# @lc app=leetcode id=1758 lang=python3
#
# [1758] Minimum Changes To Make Alternating Binary String
#

# @lc code=start
class Solution:
    def minOperations(self, s: str) -> int:
        cnt0 = 0
        cnt1 = 0
        a = True

        for i in s:
            one = i=='1'
            cnt0 += (a and one) or (not a and not one)
            cnt1 += (not a and one) or (a and not one)
            a = not a
        
        return min(cnt0, cnt1)
        
# @lc code=end


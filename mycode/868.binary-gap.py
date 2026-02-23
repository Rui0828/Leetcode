#
# @lc app=leetcode id=868 lang=python3
#
# [868] Binary Gap
#

# @lc code=start
class Solution:
    def binaryGap(self, n: int) -> int:
        
        bin_n = bin(n)[2:]
        ans = 0
        cnt = -1

        for i in range(len(bin_n)):
            if bin_n[i] == '1':
                ans = max(ans, cnt+1)
                cnt = 0
            else:
                cnt += 1
        
        return ans
        
# @lc code=end


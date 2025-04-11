#
# @lc app=leetcode id=2843 lang=python3
#
# [2843]   Count Symmetric Integers
#

# @lc code=start
class Solution:
    def countSymmetricIntegers(self, low: int, high: int) -> int:
        cnt = 0
        for i in range(low, high+1):
            s = str(i)

            if len(s) % 2:
                continue
            
            hf = len(s)//2

            if sum(int(m) for m in s[:hf]) == sum(int(m) for m in s[hf:]):
                cnt += 1
        
        return cnt
        
# @lc code=end


#
# @lc app=leetcode id=485 lang=python3
#
# [485] Max Consecutive Ones
#

# @lc code=start
class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        mx = 0
        cnt = 0
        for i in nums:
            if i == 1:
                cnt += 1
                mx = max(mx, cnt)
            else:
                cnt = 0
        return mx 
        
# @lc code=end


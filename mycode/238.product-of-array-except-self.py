#
# @lc app=leetcode id=238 lang=python3
#
# [238] Product of Array Except Self
#

# @lc code=start
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        pre = [1] * n
        suf = [1] * n

        for i in range(1, n):
            r_idx = n-i-1

            pre[i] = pre[i-1]*nums[i-1]
            suf[r_idx] = suf[r_idx+1]*nums[r_idx+1]

        return [x*y for x, y in zip(pre, suf)]
        
# @lc code=end


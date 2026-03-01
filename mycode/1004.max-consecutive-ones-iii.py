#
# @lc app=leetcode id=1004 lang=python3
#
# [1004] Max Consecutive Ones III
#

# @lc code=start
class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        
        zero_idxs = [-1]+[i for i, v in enumerate(nums) if v == 0]+[len(nums)]

        if len(zero_idxs)-2 < k:
            return len(nums)

        max_cnt = zero_idxs[k+1]-zero_idxs[0]-1

        for i in range(k+2, len(zero_idxs)):
            max_cnt = max(max_cnt, zero_idxs[i]-zero_idxs[i-k-1]-1)

        return max_cnt
# @lc code=end


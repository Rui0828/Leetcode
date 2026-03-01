#
# @lc app=leetcode id=1493 lang=python3
#
# [1493] Longest Subarray of 1's After Deleting One Element
#

# @lc code=start
class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
                
        zero_idxs = [-1]+[i for i, v in enumerate(nums) if v == 0]+[len(nums)]

        if len(zero_idxs)-2 < 1:
            return len(nums)-1

        max_cnt = zero_idxs[2]-zero_idxs[0]-2

        for i in range(3, len(zero_idxs)):
            max_cnt = max(max_cnt, zero_idxs[i]-zero_idxs[i-2]-2)

        return max_cnt

        
# @lc code=end


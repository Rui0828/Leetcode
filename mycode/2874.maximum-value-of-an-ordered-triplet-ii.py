#
# @lc app=leetcode id=2874 lang=python3
#
# [2874] Maximum Value of an Ordered Triplet II
#
from typing import List
# @lc code=start
class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        len_nums = len(nums)
        max_tri = 0
        pri_max = [0] * len_nums
        suf_max = [0] * len_nums

        pri_max[0] = nums[0]
        suf_max[len_nums-1] = nums[len_nums-1]

        for i in range(1, len_nums):
            pri_max[i] = max(nums[i], pri_max[i-1])
            suf_max[len_nums-i-1] = max(nums[len_nums-i-1], suf_max[len_nums-i])

        for j in range(1, len_nums-1):
            max_tri = max(max_tri, (pri_max[j-1] - nums[j]) * suf_max[j+1])
        
        return max_tri
        
# @lc code=end


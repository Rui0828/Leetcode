#
# @lc app=leetcode id=2873 lang=python3
#
# [2873] Maximum Value of an Ordered Triplet I
#

from typing import List
# @lc code=start
class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        len_nums = len(nums)
        max_triplets = 0
        for i in range(len_nums-2):
            for j in range(i+1, len_nums-1):
                for k in range(j+1, len_nums):
                    to_comp = (nums[i] - nums[j]) * nums[k]
                    if to_comp > max_triplets:
                        max_triplets = to_comp
        return max_triplets
        
# @lc code=end


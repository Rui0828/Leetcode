#
# @lc app=leetcode id=1863 lang=python3
#
# [1863] Sum of All Subset XOR Totals
#
from typing import List
# @lc code=start
class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        len_nums = len(nums)
        times = 2 ** (len_nums - 1)

        all_or = 0
        for i in nums:
            all_or |= i

            print(all_or)
        
        return all_or * times
# @lc code=end


#
# @lc app=leetcode id=2364 lang=python3
#
# [2364] Count Number of Bad Pairs
#

from collections import *

# @lc code=start
class Solution:
    def countBadPairs(self, nums):

        #  用扣的
        n = len(nums)
        total_pairs = n * (n - 1) // 2
        diff_count = defaultdict(int)
        for i, num in enumerate(nums):
            diff = num - i
            total_pairs -= diff_count[diff]
            diff_count[diff] += 1
        return total_pairs
        
# @lc code=end


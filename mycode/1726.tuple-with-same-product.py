#
# @lc app=leetcode id=1726 lang=python3
#
# [1726] Tuple with Same Product
#

from typing import List
import collections
import math

# @lc code=start
class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:

        cnt = 0
        rec = collections.defaultdict(int)
        lenth = len(nums)
        for i in range(lenth-1):
            for j in range(i+1, lenth):
                rec[nums[i] * nums[j]] += 1

        for i in rec.values():
            if i != 1:
                cnt += math.perm(i, 2) * 4
        
        return cnt
# @lc code=end


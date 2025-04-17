#
# @lc app=leetcode id=2176 lang=python3
#
# [2176] Count Equal and Divisible Pairs in an Array
#
from typing import List
# @lc code=start
class Solution:
    def countPairs(self, nums: List[int], k: int) -> int:
        ln = len(nums)
        cnt = 0

        for i in range(ln-1):
            for j in range(i+1, ln):
                if nums[i] == nums[j] and (i*j)%k == 0:
                    cnt += 1

        return cnt
# @lc code=end


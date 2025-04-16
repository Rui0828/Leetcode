#
# @lc app=leetcode id=2537 lang=python3
#
# [2537] Count the Number of Good Subarrays
#
from typing import List
import collections
# @lc code=start
class Solution:
    def countGood(self, nums: List[int], k: int) -> int:
        freq = collections.defaultdict(int)
        l = 0
        pairs = 0
        cnt = 0

        for r in range(len(nums)):
            v = nums[r]
            pairs += freq[v]
            freq[v] += 1

            while pairs >= k:
                cnt += len(nums) - r
                out = nums[l]
                freq[out] -= 1
                pairs -= freq[out]
                l += 1

        return cnt
                



# @lc code=end


#
# @lc app=leetcode id=1046 lang=python3
#
# [1046] Last Stone Weight
#
from heapq import *
# @lc code=start
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-i for i in stones]
        heapify(stones)

        while stones and len(stones) > 1:
            a = heappop(stones)
            b = heappop(stones)

            if a < b:
                heappush(stones, a-b)
            
        
        return -stones[0] if stones else 0
# @lc code=end


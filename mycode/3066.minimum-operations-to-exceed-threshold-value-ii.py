#
# @lc app=leetcode id=3066 lang=python3
#
# [3066] Minimum Operations to Exceed Threshold Value II
#

from typing import List
import heapq

# @lc code=start
class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        heapq.heapify(nums)

        cnt = 0
        x = heapq.heappop(nums)
        while x < k:
            cnt += 1
            y = heapq.heappop(nums)
            heapq.heappush(nums, x * 2 + y)
            
            x = heapq.heappop(nums)
        

        return cnt
        
        
# @lc code=end


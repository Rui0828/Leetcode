#
# @lc app=leetcode id=3375 lang=python3
#
# [3375] Minimum Operations to Make Array Values Equal to K
#
from typing import List
# @lc code=start
class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        hasX=0
        xMin=101
        for x in nums:
            hasX|=1<<x
            xMin=min(x, xMin)
        
        if xMin<k: return -1
        B=hasX.bit_count()
        return B-1 if xMin==k else B
        
# @lc code=end


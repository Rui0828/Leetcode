#
# @lc app=leetcode id=3162 lang=python3
#
# [3162] Find the Number of Good Pairs I
#
from typing import List
# @lc code=start
class Solution:
    def numberOfPairs(self, nums1: List[int], nums2: List[int], k: int) -> int:
        cnt = 0
        for i in nums1:
            for j in nums2:
                if j == 0:
                    continue
                elif i%(j*k) == 0:
                    cnt += 1
        
        return cnt
# @lc code=end


#
# @lc app=leetcode id=2918 lang=python3
#
# [2918] Minimum Equal Sum of Two Arrays After Replacing Zeros
#
from typing import List
# @lc code=start
class Solution:
    def minSum(self, nums1: List[int], nums2: List[int]) -> int:
        s1 = sum(nums1)
        c1 = nums1.count(0)

        s2 = sum(nums2)
        c2 = nums2.count(0)
        
        if (c1==0 and s2+c2 > s1) or (c2==0 and s1+c1 > s2):
            return -1
        
        else:
            return max(s1+c1, s2+c2)


# @lc code=end


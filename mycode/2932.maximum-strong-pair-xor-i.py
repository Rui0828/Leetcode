#
# @lc app=leetcode id=2932 lang=python3
#
# [2932] Maximum Strong Pair XOR I
#
from typing import List
# @lc code=start
class Solution:
    def maximumStrongPairXor(self, nums: List[int]) -> int:
        nums = sorted(nums)
        ln = len(nums)

        max_xor = 0
        for i in range(ln):
            for j in range(i+1, ln):
                if nums[j] - nums[i] > nums[i]:
                    break

                # print(nums[i],  nums[i], nums[i] ^ nums[j])
                max_xor = max(max_xor, nums[i] ^ nums[j])

        return max_xor
        
# @lc code=end


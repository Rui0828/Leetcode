#
# @lc app=leetcode id=3396 lang=python3
#
# [3396] Minimum Number of Operations to Make Elements in Array Distinct
#

from typing import List
import math

# @lc code=start
class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        
        dic = []
        cnt = 0

        nums.reverse()
        for i in nums:
            if i in dic:
                break
            else:
                dic.append(i)
                cnt += 1
        
        return math.ceil((len(nums) - cnt) / 3)
        
# @lc code=end


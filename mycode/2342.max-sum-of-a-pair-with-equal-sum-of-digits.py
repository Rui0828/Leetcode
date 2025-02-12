#
# @lc app=leetcode id=2342 lang=python3
#
# [2342] Max Sum of a Pair With Equal Sum of Digits
#

import collections
from typing import List

# @lc code=start
class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        max_rec = collections.defaultdict(int)

        max_value = -1

        for i in nums:
            tens = int(i/10)
            if tens == 0:
                if i not in max_rec:
                    max_rec[i] = i
                else:
                   max_value = max(max_value, i + max_rec[i]) 
                   max_rec[i] = max(max_rec[i], i)
            else:
                dg = i%10
                while tens != 0:
                    dg += tens%10
                    tens = int(tens/10)

                if dg not in max_rec:
                    max_rec[dg] = i
                else:
                    max_value = max(max_value, i + max_rec[dg])
                    max_rec[dg] = max(max_rec[dg], i)

        return max_value



        
# @lc code=end


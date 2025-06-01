#
# @lc app=leetcode id=2928 lang=python3
#
# [2928] Distribute Candies Among Children I
#
import math

# @lc code=start
class Solution:
    def distributeCandies(self, n: int, limit: int) -> int:
        
        all_cnt = math.comb(n+2, 2)
        s1 = math.comb(n-limit+1, 2) if n-limit+1 > 0 else 0
        s2 = math.comb(n-2*limit, 2) if n-2*limit > 0 else 0
        s3 = math.comb(n-3*limit-1, 2) if n-3*limit-1 > 0 else 0

        return all_cnt - 3 * s1 + 3 * s2 - s3
        
# @lc code=end


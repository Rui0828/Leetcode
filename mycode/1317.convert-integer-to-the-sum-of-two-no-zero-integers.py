#
# @lc app=leetcode id=1317 lang=python3
#
# [1317] Convert Integer to the Sum of Two No-Zero Integers
#
from typing import List
# @lc code=start
class Solution:
    def getNoZeroIntegers(self, n: int) -> List[int]:
        for i in range(1, n):
            if '0' in str(i) or '0' in str(n-i):
                continue
            return [i, n-i]
        
# @lc code=end


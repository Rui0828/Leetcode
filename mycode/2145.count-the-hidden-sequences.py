#
# @lc app=leetcode id=2145 lang=python3
#
# [2145] Count the Hidden Sequences
#
from typing import List
# @lc code=start
class Solution:
    def numberOfArrays(self, differences: List[int], lower: int, upper: int) -> int:
        mx = 0
        mn = 0
        cu = 0

        for i in differences:
            cu += i
            mx = max(mx, cu)
            mn = min(mn, cu)
        
        return max((upper-lower+1) - (mx-mn), 0)# @lc code=end


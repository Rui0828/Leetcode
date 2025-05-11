#
# @lc app=leetcode id=1550 lang=python3
#
# [1550] Three Consecutive Odds
#
from typing import List
# @lc code=start
class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        
        chk = [0] * len(arr)
        chk[0] = 1 if arr[0]%2 else 0

        for i in range(1, len(arr)):
            if arr[i]%2:
                if chk[i-1] == 2:
                    return True
                chk[i] = chk[i-1]+1
            else:
                chk[i] = 0
        
        return False

# @lc code=end


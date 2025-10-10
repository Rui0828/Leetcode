#
# @lc app=leetcode id=3147 lang=python3
#
# [3147] Taking Maximum Energy From the Mystic Dungeon
#
from typing import List
# @lc code=start
class Solution:
    def maximumEnergy(self, energy: List[int], k: int) -> int:
        
        ln_energy = len(energy)
        dp = [0]*ln_energy

        for i in range(ln_energy-1, -1, -1):
            if i > ln_energy - k -1:
                dp[i] = energy[i]
            else: 
                dp[i] = energy[i] + dp[i+k]
            
        return max(dp)
        
# @lc code=end


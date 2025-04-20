#
# @lc app=leetcode id=781 lang=python3
#
# [781] Rabbits in Forest
#
from typing import *
import collections
# @lc code=start
class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        ans = 0
        cnt = collections.defaultdict(int)

        for i in answers:
            if i == 0:
                ans += 1
                continue

            if i not in cnt:
                ans += i+1
                cnt[i] = i
            else:
                if cnt[i] == 1:
                    del cnt[i]
                else:
                    cnt[i] -= 1
        
        return ans
        
# @lc code=end


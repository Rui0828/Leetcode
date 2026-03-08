#
# @lc app=leetcode id=2390 lang=python3
#
# [2390] Removing Stars From a String
#
from collections import deque
# @lc code=start
class Solution:
    def removeStars(self, s: str) -> str:
        dq = deque()

        for i in s:
            if i != '*':
                dq.append(i)
            else:
                dq.pop()
        
        return "".join(dq)
# @lc code=end


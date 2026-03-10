#
# @lc app=leetcode id=649 lang=python3
#
# [649] Dota2 Senate
#
from collections import deque
# @lc code=start
class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        qr = deque()
        qd = deque()

        for i, j in enumerate(senate):
            if j == 'R':
                qr.append(i)
            else:
                qd.append(i)
        
        f = len(senate)
        while qr and qd:
            if qr[0] < qd[0]:
                qr.append(f)
            else:
                qd.append(f)
            qr.popleft()
            qd.popleft()
            f += 1

        return "Radiant" if qr else "Dire"
        
# @lc code=end


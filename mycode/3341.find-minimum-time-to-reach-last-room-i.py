#
# @lc app=leetcode id=3341 lang=python3
#
# [3341] Find Minimum Time to Reach Last Room I
#

import heapq
from typing import List

# @lc code=start
class Solution:
    def minTimeToReach(self, moveTime: List[List[int]]) -> int:
        N = len(moveTime)
        M = len(moveTime[0])

        time_rec = [[-1] * M for _ in range(N)]
        hp = [(0, (0, 0))]
        time_rec[0][0] = 0

        while hp:
            time, (x, y) = heapq.heappop(hp)

            if (x, y) == (N-1, M-1):
                return time
            elif time > time_rec[x][y]:
                continue
            

            for dx, dy in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                tgx, tgy = x + dx, y + dy
                if 0 <= tgx < N and 0 <= tgy < M:
                    new_time = max(time + 1, moveTime[tgx][tgy]+1)
                    if time_rec[tgx][tgy] == -1 or new_time < time_rec[tgx][tgy]:
                        time_rec[tgx][tgy] = new_time
                        heapq.heappush(hp, (new_time, (tgx, tgy)))
# @lc code=end


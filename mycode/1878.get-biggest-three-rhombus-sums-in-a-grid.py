#
# @lc app=leetcode id=1878 lang=python3
#
# [1878] Get Biggest Three Rhombus Sums in a Grid
#
import math
from heapq import *
# @lc code=start
class Solution:
    def getBiggestThree(self, grid: List[List[int]]) -> List[int]:
        n = len(grid)
        m = len(grid[0])
        top3 = []
        mxr = min(math.ceil(n/2), math.ceil(m/2))

        for r in range(mxr):
            for row in range(r, n-r):
                for col in range(m-2*r):
                    pt = (row, col)
                    cnt = grid[pt[0]][pt[1]]
                    
                    # ↗
                    ct = r
                    while ct:
                        pt = (pt[0]-1, pt[1]+1)
                        cnt += grid[pt[0]][pt[1]]
                        ct -= 1
                    
                    # ↘
                    ct = r
                    while ct:
                        pt = (pt[0]+1, pt[1]+1)
                        cnt += grid[pt[0]][pt[1]]
                        ct -= 1
                    
                    # ↙
                    ct = r
                    while ct:
                        pt = (pt[0]+1, pt[1]-1)
                        cnt += grid[pt[0]][pt[1]]
                        ct -= 1
                    
                    # ↖
                    ct = r-1
                    while ct > 0:
                        pt = (pt[0]-1, pt[1]-1)
                        cnt += grid[pt[0]][pt[1]]
                        ct -= 1
                    
                    if cnt not in top3:
                        heappush(top3, cnt)
                    while len(top3) > 3:
                        heappop(top3)

        return sorted(top3, reverse=True)
# @lc code=end


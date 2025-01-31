#
# @lc app=leetcode id=827 lang=python3
#
# [827] Making A Large Island
#

import collections
from typing import List

# @lc code=start
class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        
        
        m = len(grid)
        n = len(grid[0])
        dir = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        
        dq = collections.deque()
        water = collections.defaultdict(int)
        
        for i in range(m):
            for j in range(n):
                
                if grid[i][j] != 1:
                    continue
                
                dq.append((i, j))
                grid[i][j] = -1
                water_list = set()
                cnt = 0
                
                while dq:
                    
                    current_x, current_y = dq.pop()
                    cnt += 1
                    
                    for dx, dy in dir:
                        next_x, next_y = current_x+dx, current_y+dy
                        
                        if 0 <= next_x < m and 0 <= next_y < n:
                            if grid[next_x][next_y] == 1:
                                dq.append((next_x, next_y))
                                grid[next_x][next_y] = -1
                            elif grid[next_x][next_y] == 0:
                                water_list.add((next_x, next_y))
                            
                
                for k in water_list:
                    water[k] += cnt
                
        if water:
            return 1 + max(water.values()) 
        else:
            return 1 if grid[0][0] == 0 else m*n

# @lc code=end

print(Solution().largestIsland([[1,0],[0,1]])) # 3
print(Solution().largestIsland([[1,1],[1,0]])) # 4
print(Solution().largestIsland([[1,1],[1,1]])) # 4
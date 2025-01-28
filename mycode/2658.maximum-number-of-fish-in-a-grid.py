#
# @lc app=leetcode id=2658 lang=python
#
# [2658] Maximum Number of Fish in a Grid
#
import collections

# @lc code=start
class Solution(object):
    def findMaxFish(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        
        m = len(grid)
        n = len(grid[0])
        
        ans = 0
        dq = collections.deque()
        dir = [(1,0), (-1, 0), (0, 1), (0, -1)]
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] != 0:
                    
                    dq.append((i, j, grid[i][j]))
                    grid[i][j] = 0
                    cnt = 0
                    
                    while dq:
                        x, y, fish = dq.popleft()
                        cnt += fish
                        
                        for dx, dy in dir:
                            next_x, next_y = x + dx, y + dy
                            if 0 <= next_x < m and 0<= next_y < n:
                                if grid[next_x][next_y] != 0:
                                    dq.append((next_x, next_y, grid[next_x][next_y]))
                                    grid[next_x][next_y] = 0
                    ans = max(ans, cnt)
        return ans
# @lc code=end
print(Solution().findMaxFish([[0,2,1,0],[4,0,0,3],[1,0,0,4],[0,3,2,0]]))
print(Solution().findMaxFish([[1,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,1]]))

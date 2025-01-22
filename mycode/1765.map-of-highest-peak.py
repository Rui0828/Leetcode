#
# @lc app=leetcode id=1765 lang=python
#
# [1765] Map of Highest Peak
#

# @lc code=start
import collections

class Solution(object):
    def highestPeak(self, isWater):
        """
        :type isWater: List[List[int]]
        :rtype: List[List[int]]
        """
        
        m, n  = len(isWater), len(isWater[0])
        que = collections.deque()
        
        height = [[int(m*n)] * n for _ in range(m)]
        
        
        [que.append((i, j, 0)) for i in range(m) for j in range(n) if isWater[i][j] == 1]
        
        for i in que:
            height[i[0]][i[1]] = 0
        
        # print(que)
        
        dir = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        
        while que:
            
            i, j, h  = que.popleft()
            
            for x, y in dir:
                tx, ty = x+i, y+j
                
                if 0 <= tx < m and 0 <= ty < n and h+1 < height[tx][ty]:
                        height[tx][ty] = h+1
                        que.append((tx, ty, h+1))
            
        return height
        
# @lc code=end

print(Solution().highestPeak([[0,1],[0,0]]))
print(Solution().highestPeak([[0,0,1],[1,0,0],[0,0,0]]))
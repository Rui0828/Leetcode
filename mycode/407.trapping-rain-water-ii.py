#
# @lc app=leetcode id=407 lang=python
#
# [407] Trapping Rain Water II
#

# @lc code=start
import heapq

class Solution(object):
    def trapRainWater(self, heightMap):
        """
        :type heightMap: List[List[int]]
        :rtype: int
        """
        m = len(heightMap)
        n = len(heightMap[0])
        
        # 紀錄格子狀態
        rec = [[0 for _ in range(n)] for _ in range(m) ]
        ## 狀態：
        ## 0 還未看過
        ## 1 牆壁，候選掃描起始點(heap)
        
        # 四周先設成 1，並加入 wall (heap)
        cnt = 0
        wall = []
        for i in range(m):
            if i==0 or i==m-1:
                for j in range(n):
                    rec[i][j] = 1
                    heapq.heappush(wall, (heightMap[i][j], [i, j]))
            else:
                rec[i][0] = 1
                heapq.heappush(wall, (heightMap[i][0], [i, 0]))
                rec[i][n-1] = 1
                heapq.heappush(wall, (heightMap[i][n-1], [i, n-1]))
                
        # Explore neighbors
        while wall:
            
            height, [current_i, current_j] = heapq.heappop(wall)
            dir = [(0, 1), (0, -1), (1, 0), (-1, 0)]

            for dir_i, dir_j in dir:
                next_i, next_j = current_i+dir_i, current_j+dir_j
                
                if 1 <= next_i < m-1 and 1 <= next_j < n-1 and rec[next_i][next_j] == 0:
                    if heightMap[next_i][next_j] >= height:
                        rec[next_i][next_j] = 1
                        heapq.heappush(wall, (heightMap[next_i][next_j], [next_i, next_j]))
                    else:
                        cnt += height - heightMap[next_i][next_j]
                        rec[next_i][next_j] = 1
                        heapq.heappush(wall, (height, [next_i, next_j]))
            
            # print(height, current_i, current_j)
            # print(wall)
            # for i in range(m):
            #     print(rec[i])
            # print("-"*100)
        return cnt
# @lc code=end

print(Solution().trapRainWater([[1,4,3,1,3,2],[3,2,1,3,2,4],[2,3,3,2,3,1]])) # 3
print(Solution().trapRainWater([[3,3,3,3,3],[3,2,2,2,3],[3,2,1,2,3],[3,2,2,2,3],[3,3,3,3,3]])) # 10


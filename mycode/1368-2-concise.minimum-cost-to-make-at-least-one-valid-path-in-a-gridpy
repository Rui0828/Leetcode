#
# @lc app=leetcode id=1368 lang=python
#
# [1368] Minimum Cost to Make at Least One Valid Path in a Grid
#

# @lc code=start
import collections

class Solution(object):
    def minCost(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        
        m, n = len(grid), len(grid[0])
        dir = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        
        # dijkstra algorithm
        min_cost = [[int(1e9) for _ in range(n)] for _ in range(m)]
        min_cost[0][0] = 0
        queue = collections.deque([(0, [0, 0])])
        
        while queue:
            
            current_cost, [current_i, current_j] = queue.popleft()
            
            if current_i == m-1 and current_j ==  n-1:
                return current_cost
            
            # Explore neighbors
            for dir_code, (dir_i, dir_j) in enumerate(dir):
                next_i, next_j = current_i+dir_i, current_j+dir_j
                cost = current_cost if grid[current_i][current_j] == dir_code+1 else current_cost+1
            
                if 0 <= next_i < m and 0 <= next_j < n and cost < min_cost[next_i][next_j]:
                    min_cost[next_i][next_j] = cost
                    if cost==current_cost:
                        queue.appendleft((cost, [next_i, next_j]))
                    else:
                        queue.append((cost, [next_i, next_j]))
        return min_cost[m-1][n-1]


# @lc code=end

print(Solution().minCost([[1,1,1,1],[2,2,2,2],[1,1,1,1],[2,2,2,2]])) # 3
print(Solution().minCost([[1,1,3],[3,2,2],[1,1,4]])) # 0
print(Solution().minCost([[1,2],[4,3]])) # 1
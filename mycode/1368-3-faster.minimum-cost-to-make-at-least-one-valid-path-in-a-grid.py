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
        
        m = len(grid)
        n = len(grid[0])
        
        # dijkstra algorithm
        min_cost = [[int(1e9) for _ in range(n)] for _ in range(m)]
        min_cost[0][0] = 0
        queue = collections.deque([(0, [0, 0])])
        
        while queue:
            
            current_cost, [current_i, current_j] = queue.popleft()
            
            if current_i == m-1 and current_j ==  n-1:
                return current_cost
            
            # Explore neighbors
            ## right
            if current_j != n-1:
                if grid[current_i][current_j] == 1:
                    cost = current_cost
                else:
                    cost = current_cost + 1
                
                if cost < min_cost[current_i][current_j+1]:
                    min_cost[current_i][current_j+1] = cost
                    if cost==current_cost:
                        queue.appendleft((cost, [current_i, current_j+1]))
                    else: 
                        queue.append((cost, [current_i, current_j+1]))

            ## left
            if current_j != 0:
                if grid[current_i][current_j] == 2:
                    cost = current_cost
                else:
                    cost = current_cost + 1
                
                if cost < min_cost[current_i][current_j-1]:
                    min_cost[current_i][current_j-1] = cost
                    if cost==current_cost:
                        queue.appendleft((cost, [current_i, current_j-1]))
                    else: 
                        queue.append((cost, [current_i, current_j-1]))
                    
            
            ## lower
            if current_i != m-1:
                if grid[current_i][current_j] == 3:
                    cost = current_cost
                else:
                    cost = current_cost + 1
                
                if cost < min_cost[current_i+1][current_j]:
                    min_cost[current_i+1][current_j] = cost
                    if cost==current_cost:
                        queue.appendleft((cost, [current_i+1, current_j]))
                    else: 
                        queue.append((cost, [current_i+1, current_j]))
                    
            ## upper 
            if current_i != 0:
                if grid[current_i][current_j] == 4:
                    cost = current_cost
                else:
                    cost = current_cost + 1
                
                if cost < min_cost[current_i-1][current_j]:
                    min_cost[current_i-1][current_j] = cost
                    if cost==current_cost:
                        queue.appendleft((cost, [current_i-1, current_j]))
                    else: 
                        queue.append((cost, [current_i-1, current_j]))
        
        return min_cost[m-1][n-1]


# @lc code=end

print(Solution().minCost([[1,1,1,1],[2,2,2,2],[1,1,1,1],[2,2,2,2]])) # 3
print(Solution().minCost([[1,1,3],[3,2,2],[1,1,4]])) # 0
print(Solution().minCost([[1,2],[4,3]])) # 1
#
# @lc app=leetcode id=1267 lang=python
#
# [1267] Count Servers that Communicate
#

# @lc code=start
class Solution(object):
    def countServers(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        
        s_cnt = 0
        
        len_grid = len(grid)
        for i in range(len_grid):
            r = grid[i]
            if sum(r) == 1:
                j = r.index(1)
                if sum([grid[k][j] for k in range(len_grid)]) == 1:
                    s_cnt += 1
                
        all_cnt = sum([sum(i) for i in grid])
        return all_cnt - s_cnt
        
# @lc code=end
print("="*10)
print(Solution().countServers([[1,0],[0,1]])) # 0
print("="*10)
print(Solution().countServers([[1,0],[1,1]])) # 3
print("="*10)
print(Solution().countServers([[1,1,0,0],[0,0,1,0],[0,0,1,0],[0,0,0,1]])) # 4

#
# @lc app=leetcode id=2965 lang=python3
#
# [2965] Find Missing and Repeated Values
#

from typing import List
import collections

# @lc code=start
class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        grid_len = len(grid)
        num_rec = collections.deque([i+1 for i in range(grid_len*grid_len)])
        repeating = -1
        missing = -1
        
        for i in range(grid_len):
            for j in range(grid_len):
                if grid[i][j] in num_rec:
                    num_rec.remove(grid[i][j])
                else:
                    repeating = grid[i][j]
        
        missing = num_rec[0]
        
        return [repeating, missing]
        
# @lc code=end


#
# @lc app=leetcode id=1536 lang=python3
#
# [1536] Minimum Swaps to Arrange a Binary Grid
#

# @lc code=start
class Solution:
    def minSwaps(self, grid: List[List[int]]) -> int:
        n = len(grid)
        zcnt = []
        for row in range(n):
            idx = 0
            while not grid[row][n-idx-1] and idx != n:
                idx += 1
            zcnt.append(idx)

        swap = 0
        for i in range(n-1, 0, -1):
            match = False
            for j, v in enumerate(zcnt):
                if v >= i:
                    swap += j
                    del zcnt[j]
                    match = True
                    break
            if not match:
                return -1
        
        return swap

        
# @lc code=end


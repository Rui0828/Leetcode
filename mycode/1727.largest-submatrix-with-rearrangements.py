#
# @lc app=leetcode id=1727 lang=python3
#
# [1727] Largest Submatrix With Rearrangements
#

# @lc code=start
class Solution:
    def largestSubmatrix(self, matrix: List[List[int]]) -> int:
        m = len(matrix)
        n = len(matrix[0])
        mx = 0

        for i in range(m):
            if i != 0:
                for j in range(n):
                    if matrix[i][j] == 1:
                        matrix[i][j] = matrix[i-1][j] + 1
        
        for i in range(m):  
            matrix[i].sort(reverse=True)
            for j in range(n):
                if matrix[i][j] == 0:
                    break
                else:
                    mx = max(mx, (j+1)*matrix[i][j])
            
        return mx
        
# @lc code=end


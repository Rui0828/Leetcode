#
# @lc app=leetcode id=2661 lang=python
#
# [2661] First Completely Painted Row or Column
#

# @lc code=start
class Solution(object):
    def firstCompleteIndex(self, arr, mat):
        """
        :type arr: List[int]
        :type mat: List[List[int]]
        :rtype: int
        """
        m  = len(mat)
        n = len(mat[0])
        
        pos = {mat[i][j]:[i, j] for i in range(m) for j in range(n)}
        
        row_cnt = [0] * m
        col_cnt = [0] * n
        
        for i in range(len(arr)):
            r = pos[arr[i]][0]
            c = pos[arr[i]][1]
            
            row_cnt[r] += 1
            col_cnt[c] += 1
            
            if n == row_cnt[r] or m == col_cnt[c]:
                return i 
# @lc code=end

print(Solution().firstCompleteIndex([1,3,4,2], [[1,4],[2,3]]))
print("-"*100)
print(Solution().firstCompleteIndex([2,8,7,4,1,3,5,6,9], [[3,2,5],[1,4,6],[8,7,9]]))
print("-"*100)
print(Solution().firstCompleteIndex([1,4,5,2,6,3], [[4,3,5],[1,2,6]]))
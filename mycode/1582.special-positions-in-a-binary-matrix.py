#
# @lc app=leetcode id=1582 lang=python3
#
# [1582] Special Positions in a Binary Matrix
#

# @lc code=start
class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        
        cnt = 0
        for i in range(len(mat)):
            if sum(mat[i]) == 1:
                if sum([j[mat[i].index(1)] for j in mat]) == 1:
                    cnt += 1
        
        return cnt
        
# @lc code=end


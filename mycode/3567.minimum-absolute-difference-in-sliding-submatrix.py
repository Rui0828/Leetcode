#
# @lc app=leetcode id=3567 lang=python3
#
# [3567] Minimum Absolute Difference in Sliding Submatrix
#

# @lc code=start
class Solution:
    def minAbsDiff(self, grid: List[List[int]], k: int) -> List[List[int]]:
        
        ans = []

        for i in range(len(grid)-k+1):
            tmp = []
            for j in range(len(grid[0])-k+1):
                if k == 1:
                    tmp.append(0)
                else:
                    tmp2 = sorted(list(set([grid[a][b] for a in range(i, i+k) for b in range(j, j+k)])))
                    if len(tmp2)>1:
                        mn = abs(tmp2[1]-tmp2[0])
                        for a in range(1, len(tmp2)-1):
                            mn = min(mn, abs(tmp2[a+1]-tmp2[a]))
                        tmp.append(mn)
                    else:
                        tmp.append(0)
            ans.append(tmp)
        
        return ans
# @lc code=end


#
# @lc app=leetcode id=118 lang=python
#
# [118] Pascal's Triangle
#

# @lc code=start
class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        
        ans = [[1]]
        
        if numRows == 1:
            return ans
        else:
            numRows -= 1
            while numRows:
                temp = [1]
                for i in range(len(ans[-1])-1):
                    temp.append(ans[-1][i] + ans[-1][i+1])
                temp.append(1)
                ans.append(temp)
                numRows -= 1
        return ans
# @lc code=end

print(Solution().generate(5))
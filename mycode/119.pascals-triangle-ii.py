#
# @lc app=leetcode id=119 lang=python
#
# [119] Pascal's Triangle II
#

# @lc code=start
class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        ans = [1]
        
        if rowIndex == 0:
            return ans
        else:
            while rowIndex:
                temp = [1]
                for i in range(len(ans)-1):
                    temp.append(ans[i] + ans[i+1])
                temp.append(1)
                ans = temp
                rowIndex -= 1
        return ans
# @lc code=end

print(Solution().getRow(3))
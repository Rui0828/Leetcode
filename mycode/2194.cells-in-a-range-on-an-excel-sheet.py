#
# @lc app=leetcode id=2194 lang=python
#
# [2194] Cells in a Range on an Excel Sheet
#

# @lc code=start
class Solution(object):
    def cellsInRange(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        return [chr(i) + str(j) for i in range(ord(s[0]), ord(s[3])+1) for j in range(int(s[1]), int(s[4])+1)]
        
        # ans = []
        # for i in range(ord(s[0]), ord(s[3])+1):
        #     for j in range(int(s[1]), int(s[4])+1):
        #         ans.append(chr(i) + str(j))
        # return ans
    
        # return [chr(i) + str(j) for i in range(ord(s[0]), ord(s[3])+1) for j in range(int(s[1]), int(s[4])+1)]
        
# @lc code=end

print(Solution().cellsInRange("K1:L2"))
print(Solution().cellsInRange("A1:F1"))
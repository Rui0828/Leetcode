#
# @lc app=leetcode id=67 lang=python
#
# [67] Add Binary
#

# @lc code=start
class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        
        a = int(a, 2)
        b = int(b, 2)
        
        ans = str(bin(a+b))
        
        return ans[2:]
    
# @lc code=end

print(Solution().addBinary("11", "1"))
print(Solution().addBinary("1010", "1011"))


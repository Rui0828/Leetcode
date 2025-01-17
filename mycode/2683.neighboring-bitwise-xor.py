#
# @lc app=leetcode id=2683 lang=python
#
# [2683] Neighboring Bitwise XOR
#

# @lc code=start
class Solution(object):
    def doesValidArrayExist(self, derived):
        """
        :type derived: List[int]
        :rtype: bool
        """
        
        ans = derived[0]
        for i in range(1, len(derived)):
            ans = ans ^ derived[i]
        
        return ans == 0
# @lc code=end


#
# @lc app=leetcode id=3174 lang=python
#
# [3174] Clear Digits
#

# @lc code=start
class Solution(object):
    def clearDigits(self, s):
        """
        :type s: str
        :rtype: str
        """
        
        ans = []

        for i in s:
            if i.isdigit() and ans:
                ans.pop()
            else:
                ans.append(i)
        
        return "".join(ans)

# @lc code=end


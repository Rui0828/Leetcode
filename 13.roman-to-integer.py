#
# @lc app=leetcode id=13 lang=python
#
# [13] Roman to Integer
#

# @lc code=start
class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        ans = 0
        
        table = {'I':1, 
                 'V':5, 
                 'X':10,
                 'L':50,
                 'C':100,
                 'D':500, 
                 'M':1000}
        s = list(s)
        s_turn = [table[i] for i in s]
        
        for i in range(len(s_turn)-1):
            if s_turn[i] < s_turn[i+1]:
                ans -= s_turn[i]
            else:
                ans += s_turn[i]
        ans += s_turn[-1]
        return ans
# @lc code=end


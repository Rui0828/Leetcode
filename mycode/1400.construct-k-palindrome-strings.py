#
# @lc app=leetcode id=1400 lang=python
#
# [1400] Construct K Palindrome Strings
#

# @lc code=start
class Solution(object):
    def canConstruct(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: bool
        """
        
        if len(s) < k:
            return False
        
        ch = {}
        odd = 0
        for i in list(s):
            if i in ch:
                ch[i] += 1
            else:
                ch[i] = 1
        
        for i in ch.values():
            if i % 2 != 0:
                odd += 1
        
        if odd > k:
            return False
        else:
            return True
        
        
        
# @lc code=end

print(Solution().canConstruct("annabelle", 2))
print(Solution().canConstruct("leetcode", 3))
print(Solution().canConstruct("true", 4))
print(Solution().canConstruct("cr", 7))
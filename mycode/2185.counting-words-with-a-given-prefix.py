#
# @lc app=leetcode id=2185 lang=python
#
# [2185] Counting Words With a Given Prefix
#

# @lc code=start
class Solution(object):
    def prefixCount(self, words, pref):
        """
        :type words: List[str]
        :type pref: str
        :rtype: int
        """
        ans = 0
        for i in words:
            if i.startswith(pref):
                ans += 1
        return ans
# @lc code=end


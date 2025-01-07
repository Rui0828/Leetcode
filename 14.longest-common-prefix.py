#
# @lc app=leetcode id=14 lang=python
#
# [14] Longest Common Prefix
#

# @lc code=start
class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        ans = ""
        strs = sorted(strs)
        
        head = strs[0]
        tail = strs[-1]
        
        for i in range(min(len(head), len(tail))):
            if head[i] == tail[i]:
                ans += head[i]
            else:
                return ans
        return ans
# @lc code=end


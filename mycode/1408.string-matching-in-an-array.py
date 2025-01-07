#
# @lc app=leetcode id=1408 lang=python
#
# [1408] String Matching in an Array
#

# @lc code=start
class Solution(object):
    def stringMatching(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        ans = set()
        for i in words:
            for j in words:
                if i == j:
                    continue
                else:
                    if i in j:
                        ans.add(i)
        return list(ans)
        
        
# @lc code=end


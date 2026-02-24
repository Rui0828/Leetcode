#
# @lc app=leetcode id=1768 lang=python3
#
# [1768] Merge Strings Alternately
#

# @lc code=start
class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        ans = ""
        for i in range(max(len(word1), len(word2))):
            if i < len(word1):
                ans += word1[i]
            if i < len(word2):
                ans += word2[i]
        
        return ans
        
# @lc code=end


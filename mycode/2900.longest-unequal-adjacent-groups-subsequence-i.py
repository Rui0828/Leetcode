#
# @lc app=leetcode id=2900 lang=python3
#
# [2900] Longest Unequal Adjacent Groups Subsequence I
#
from typing import List
# @lc code=start
class Solution:
    def getLongestSubsequence(self, words: List[str], groups: List[int]) -> List[str]:
        g = groups[0]
        ans = [words[0]]

        for i in range(1, len(words)):
            if groups[i] != g:
                ans.append(words[i])
                g = groups[i]
        
        return ans
# @lc code=end


#
# @lc app=leetcode id=2901 lang=python3
#
# [2901] Longest Unequal Adjacent Groups Subsequence II
#
from typing import List
# @lc code=start
class Solution:
    def getWordsInLongestSubsequence(self, words: List[str], groups: List[int]) -> List[str]:
        
        ln = len(words)
        cnt = [[] for _ in range(ln)]


        for i in range(ln):
            for j in range(0, i):
                if groups[i] != groups[j] and len(words[i]) == len(words[j]):
                    hd = 0
                    for k in range(len(words[i])):
                        if words[i][k] != words[j][k]:
                            hd += 1
                    if hd == 1:
                        if len(cnt[j])+1 > len(cnt[i]):
                            cnt[i] = cnt[j] + [words[i]]
            if not cnt[i]:
                cnt[i] = [words[i]]
        
        return max(cnt, key=len)

        
# @lc code=end


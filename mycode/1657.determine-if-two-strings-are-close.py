#
# @lc app=leetcode id=1657 lang=python3
#
# [1657] Determine if Two Strings Are Close
#
from collections import Counter
# @lc code=start
class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        return sorted(Counter(word1).values())==sorted(Counter(word2).values()) and set(Counter(word1).keys())==set(Counter(word2).keys())
# @lc code=end


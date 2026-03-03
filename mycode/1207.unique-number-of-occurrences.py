#
# @lc app=leetcode id=1207 lang=python3
#
# [1207] Unique Number of Occurrences
#
from collections import Counter
# @lc code=start
class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool: 
        cnt = Counter(arr)
        return len(set(cnt.keys())) == len(set(cnt.values()))
# @lc code=end


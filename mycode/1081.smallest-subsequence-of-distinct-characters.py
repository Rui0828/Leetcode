#
# @lc app=leetcode id=1081 lang=python3
#
# [1081] Smallest Subsequence of Distinct Characters
#
from collections import defaultdict
# @lc code=start
class Solution:
    def smallestSubsequence(self, s: str) -> str:
        n = len(s)
        d = defaultdict(int)
        q = []

        for i,c in enumerate(s):
            d[c] = max(d[c], i)

        for i,c in enumerate(s):
            if c in q:
                continue

            while q and c < q[-1] and d[q[-1]] > i:
                q.pop()

            q.append(c)

        return "".join(q)
# @lc code=end


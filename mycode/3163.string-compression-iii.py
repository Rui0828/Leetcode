#
# @lc app=leetcode id=3163 lang=python3
#
# [3163] String Compression III
#
from collections import defaultdict
# @lc code=start
class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
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


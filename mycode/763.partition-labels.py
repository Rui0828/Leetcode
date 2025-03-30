#
# @lc app=leetcode id=763 lang=python3
#
# [763] Partition Labels
#

# @lc code=start
from typing import List
import collections

class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        endidx = collections.defaultdict(int)
        ans = []
        
        for i in range(len(s)):
            endidx[s[i]] = i
        
        start = end = 0
        for i in range(len(s)):
            if endidx[s[i]] > end:
                end = endidx[s[i]]

            if i == end:
                ans.append(end - start + 1)
                start = i + 1
        
        return ans
# @lc code=end

print(Solution().partitionLabels("ababcbacadefegdehijhklij"))
print(Solution().partitionLabels("eccbbbbdec"))
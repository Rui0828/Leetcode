#
# @lc app=leetcode id=386 lang=python3
#
# [386] Lexicographical Numbers
#
from typing import List
# @lc code=start
class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        return [int(j) for j in sorted([str(i+1) for i in range(n)])]
# @lc code=end


#
# @lc app=leetcode id=3666 lang=python3
#
# [3666] Minimum Operations to Equalize Binary String
#

# @lc code=start
import math

class Solution:
    def minOperations(self, s: str, k: int) -> int:
        n = len(s)
        z = s.count('0')

        if z == 0:
            return 0
        if n == k:
            return 1 if z == n else -1

        b = n - k
        candidates = []

        if k % 2 == z % 2:
            m_odd = max(math.ceil(z / k), math.ceil((n - z) / b))
            m_odd += ~m_odd & 1
            candidates.append(m_odd)

        if z % 2 == 0:
            m_even = max(math.ceil(z / k), math.ceil(z / b))
            m_even += m_even & 1
            candidates.append(m_even)

        return min(candidates) if candidates else -1
        
# @lc code=end

#
# @lc app=leetcode id=739 lang=python3
#
# [739] Daily Temperatures
#
from collections import deque
# @lc code=start
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        dq = deque()
        ans = [0] * n
        
        for i in range(n):
            while dq and temperatures[dq[-1]] < temperatures[i]:
                idx = dq.pop()
                ans[idx] += i - idx
            dq.append(i)
        
        return ans

        
# @lc code=end


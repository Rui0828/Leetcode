#
# @lc app=leetcode id=2140 lang=python3
#
# [2140] Solving Questions With Brainpower
#

from typing import List

# @lc code=start
class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        len_q = len(questions)
        dp = [0]*len_q

        for i in range(len_q-1, -1, -1):
            if i + questions[i][1]+1 > len_q-1:
                to_cmp = questions[i][0]
            else:
                to_cmp = questions[i][0]+dp[i+questions[i][1]+1]

            if i == len_q-1 or to_cmp > dp[i+1]:
                dp[i] = to_cmp
            else:
                dp[i] = dp[i+1]
        return dp[0]
# @lc code=end


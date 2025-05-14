#
# @lc app=leetcode id=3337 lang=python3
#
# [3337] Total Characters in String After Transformations II
#

# @lc code=start
import numpy as np
from typing import List

class Solution:
    def lengthAfterTransformations(self, s: str, t: int, nums: List[int]) -> int:
        MOD = 10**9 + 7
        mat = np.zeros((26, 26), dtype=object)

        for i in range(26):
            for j in range(i+1, i+1+nums[i]):
                tg = j % 26
                mat[i][tg] = 1
        
        mat_all = np.identity(26, dtype=object)
        while t > 0:
            if t % 2:
                mat_all = np.dot(mat_all, mat) % MOD
            mat = np.dot(mat, mat) % MOD
            t //= 2

        ans = np.zeros(26, dtype=object)
        for i in list(s):
            ans[ord(i) - ord('a')] += 1
        
        ans = np.dot(ans, mat_all) % MOD

        return int(sum(ans) % MOD)
# @lc code=end


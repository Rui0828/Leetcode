#
# @lc app=leetcode id=3130 lang=python3
#
# [3130] Find All Possible Stable Binary Arrays II
#

# @lc code=start
class Solution:
    def numberOfStableArrays(self, zero: int, one: int, limit: int) -> int:
        MOD = 10**9 + 7

        dp0 = [[0]*(one+1) for _ in range(zero+1)] # dp0 結尾為 ~ limit 個 0 方法數
        dp1 = [[0]*(one+1) for _ in range(zero+1)] # dp1 結尾為 ~ limit 個 1 方法數

        for i in range(1, min(limit, zero)+1): # 前面沒東西，只有 i 個 0
            dp0[i][0] = 1
        for j in range(1, min(limit, one)+1): # 前面沒東西，只有 j 個 1
            dp1[0][j] = 1

        # zeros 要找結尾 1，用 dp0 抓 dp1 橫向
        # ones 要找結尾 0，用 dp1 抓 dp 0 橫向
        for z in range(1, zero+1):
            for o in range(1, one+1):

                dp0[z][o] = dp0[z-1][o] + dp1[z-1][o]
                if z > limit:
                    dp0[z][o] -= dp1[z-limit-1][o]

                dp1[z][o] = dp1[z][o-1] + dp0[z][o-1]
                if o > limit:
                    dp1[z][o] -= dp0[z][o-limit-1]

        return (dp0[zero][one] + dp1[zero][one]) % MOD
        
# @lc code=end


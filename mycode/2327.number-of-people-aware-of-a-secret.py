#
# @lc app=leetcode id=2327 lang=python3
#
# [2327] Number of People Aware of a Secret
#

# @lc code=start
class Solution:
    def peopleAwareOfSecret(self, n: int, delay: int, forget: int) -> int:
        
        MOD = 10**9 + 7

        dp = [[0] * forget for _ in range(n)]

        dp[0][0] = 1
        for i in range(1, n):
            for j in range(forget):

                if j==0:
                    dp[i][j] = sum(dp[i-1][delay-1:-1]) % MOD
                
                else:
                    dp[i][j] = dp[i-1][j-1] % MOD
        
        return sum(dp[n-1]) % MOD

        
# @lc code=end


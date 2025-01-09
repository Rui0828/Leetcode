#
# @lc app=leetcode id=115 lang=python
#
# [115] Distinct Subsequences
#

# @lc code=start
class Solution(object):
    def numDistinct(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: int
        """

        len_s = len(s)
        len_t = len(t)
        
        dp  = [list() for _ in range(len_t)]
        
        for i in range(len_t):
            if i==0:
                cnt = 0
                for j in range(len_s):
                    if t[i] == s[j]:
                        cnt += 1
                    dp[i].append(cnt)
            else:
                for j in range(len_s):
                    if j<i:
                        dp[i].append(0)
                    else:
                        if t[i] == s[j]:
                            dp[i].append(dp[i-1][j-1] + dp [i][j-1])
                        else:
                            dp[i].append(dp[i][j-1])
        
        return dp[len_t-1][len_s-1]
        
# @lc code=end

print(Solution().numDistinct("rabbbit", "rabbit"))
print(Solution().numDistinct("babgbag", "bag"))



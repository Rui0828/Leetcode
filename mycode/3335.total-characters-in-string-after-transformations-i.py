#
# @lc app=leetcode id=3335 lang=python3
#
# [3335] Total Characters in String After Transformations I
#

# @lc code=start
class Solution:
    def lengthAfterTransformations(self, s: str, t: int) -> int:
        cnt = [0] * 26
        MOD = 10**9 + 7

        for c in s:
            cnt[ord(c) - ord('a')] += 1

        while(t):
            tmp = [0]*26

            for i in range(26):
                if i==25:
                    tmp[0] = (tmp[0] + cnt[i]) % MOD
                    tmp[1] = (tmp[1] + cnt[i]) % MOD
                else:
                    tmp[i + 1] = (tmp[i + 1] + cnt[i]) % MOD
            cnt = tmp
            t -= 1
        return sum(cnt) % MOD
        
# @lc code=end


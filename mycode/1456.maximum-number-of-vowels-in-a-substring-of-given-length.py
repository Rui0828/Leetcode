#
# @lc app=leetcode id=1456 lang=python3
#
# [1456] Maximum Number of Vowels in a Substring of Given Length
#

# @lc code=start
class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = set("aeiou")
        c_cnt = sum(c in vowels for c in s[:k])
        max_cnt = c_cnt

        for i in range(k, len(s)):
            c_cnt += (s[i] in vowels) - (s[i-k] in vowels)
            max_cnt = max(max_cnt, c_cnt)
        
        return max_cnt

        
# @lc code=end


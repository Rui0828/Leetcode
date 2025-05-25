#
# @lc app=leetcode id=2131 lang=python3
#
# [2131] Longest Palindrome by Concatenating Two Letter Words
#
import collections
from typing import List
# @lc code=start
class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        freq = collections.Counter(words)
        cnt = 0
        dchk = False

        print(freq)

        for k in freq:
            if k[0]==k[1]:
                if not dchk and freq[k]%2:
                    dchk = True
                cnt += freq[k]//2*2
            else:
                cnt += min(freq[k], freq[k[1]+k[0]])

        return cnt*2+2 if dchk else cnt*2
# @lc code=end


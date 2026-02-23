#
# @lc app=leetcode id=1461 lang=python3
#
# [1461] Check If a String Contains All Binary Codes of Size K
#

# @lc code=start
class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:

        a = set()
        for i in range(len(s) - k + 1):
            a.add(s[i:i+k])

        return len(a)==2**k
        
# @lc code=end


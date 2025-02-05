#
# @lc app=leetcode id=1790 lang=python3
#
# [1790] Check if One String Swap Can Make Strings Equal
#
# @lc code=start
class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        if s1==s2:
            return True
        else:
            chk1 = chk2 = ""
            for i, j in zip(s1, s2):
                if i != j:
                    chk1 = chk1 + i
                    chk2 = j + chk2
            return len(chk1)==2 and chk1==chk2
        
# @lc code=end


#
# @lc app=leetcode id=1071 lang=python3
#
# [1071] Greatest Common Divisor of Strings
#

# @lc code=start
class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        
        from math import gcd
        if str1+str2 != str2+str1:
            return ""

        else:
            len_gcd = gcd(len(str1), len(str2))
            
            return str1[:len_gcd]
        
# @lc code=end


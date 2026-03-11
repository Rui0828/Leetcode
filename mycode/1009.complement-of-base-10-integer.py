#
# @lc app=leetcode id=1009 lang=python3
#
# [1009] Complement of Base 10 Integer
#

# @lc code=start
class Solution:
    def bitwiseComplement(self, n: int) -> int:
        return n ^ ((1 << n.bit_length()) - 1) if n else 1
        
# @lc code=end


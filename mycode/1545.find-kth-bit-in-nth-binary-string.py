#
# @lc app=leetcode id=1545 lang=python3
#
# [1545] Find Kth Bit in Nth Binary String
#

# @lc code=start
class Solution:
    def findKthBit(self, n: int, k: int) -> str:  
        s = '0'
        while len(s) < k:
            s = s + '1' + s.translate(str.maketrans("01", "10"))[::-1]

        return s[k-1]

# @lc code=end


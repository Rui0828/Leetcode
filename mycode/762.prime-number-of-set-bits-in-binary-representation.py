#
# @lc app=leetcode id=762 lang=python3
#
# [762] Prime Number of Set Bits in Binary Representation
#

# @lc code=start
class Solution:
    def countPrimeSetBits(self, left: int, right: int) -> int:

        cnt = 0
        for i in range(left, right+1):
            if i.bit_count() in [2, 3, 5, 7, 11, 13, 17, 19]:
                cnt += 1

        return cnt
# @lc code=end


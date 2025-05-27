#
# @lc app=leetcode id=2894 lang=python3
#
# [2894] Divisible and Non-divisible Sums Difference
#

# @lc code=start
class Solution:
    def differenceOfSums(self, n: int, m: int) -> int:
        dbm = ndbm = 0

        for i in range(1, n+1):
            if i % m == 0:
                dbm += i
            else:
                ndbm += i
        
        return ndbm - dbm
# @lc code=end


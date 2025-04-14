#
# @lc app=leetcode id=1534 lang=python3
#
# [1534] Count Good Triplets
#
from typing import List
# @lc code=start
class Solution:
    def countGoodTriplets(self, arr: List[int], a: int, b: int, c: int) -> int:
        ln = len(arr)
        cnt = 0
        for i in range(ln-2):
            for j in range(i+1, ln-1):
                for k in range(j+1, ln):
                    if abs(arr[i]-arr[j]) <= a and abs(arr[j]-arr[k]) <= b and abs(arr[i]-arr[k]) <= c:
                        cnt += 1

        return cnt
# @lc code=end


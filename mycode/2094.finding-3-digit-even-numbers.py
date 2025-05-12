#
# @lc app=leetcode id=2094 lang=python3
#
# [2094] Finding 3-Digit Even Numbers
#
from collections import Counter
from typing import List
# @lc code=start
class Solution:
    def findEvenNumbers(self, digits: List[int]) -> List[int]:
        
        freq=Counter(digits)
        ans=[]

        for i in range(100, 1000, 2):
            x1, x2, x3 = i//100, (i//10)%10, i%10

            chk = freq.copy()

            chk[x1]-=1
            chk[x2]-=1
            chk[x3]-=1

            if chk[x1] >= 0 and chk[x2] >= 0 and chk[x3] >= 0:
                ans.append(i)
        
        return ans
# @lc code=end


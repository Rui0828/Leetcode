#
# @lc app=leetcode id=645 lang=python3
#
# [645] Set Mismatch
#
from collections import Counter
# @lc code=start
class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        cnt = Counter(nums)
        rep = los = 0
        for i in range(1, len(nums)+1):
            if rep and los:
                break
            if cnt[i] == 2:
                rep = i
            elif cnt[i] == 0:
                los = i
        
        return [rep, los]
        
# @lc code=end


#
# @lc app=leetcode id=1679 lang=python3
#
# [1679] Max Number of K-Sum Pairs
#
from collections import Counter
# @lc code=start
class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:

        cnt = Counter()
        ans = 0
        
        for x in nums:
            if cnt[k-x] > 0:
                ans += 1
                cnt[k-x] -= 1
            else:
                cnt[x] += 1
        return ans
        
# @lc code=end


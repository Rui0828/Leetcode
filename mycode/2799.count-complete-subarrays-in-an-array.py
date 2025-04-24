#
# @lc app=leetcode id=2799 lang=python3
#
# [2799] Count Complete Subarrays in an Array
#
from typing import List
import collections
# @lc code=start
class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        cnt = collections.defaultdict(int)

        us = set(nums)
        chk = 0

        while(us):
            num = nums[chk]
            cnt[num] += 1
            if num in us:
                us.remove(num)
            chk += 1
        
        ans = 0
        start = 0

        cnt[nums[chk-1]] -= 1
        for i in range(chk-1, len(nums)):
            cnt[nums[i]] += 1
            while cnt[nums[start]] > 1:
                cnt[nums[start]] -= 1
                start += 1

            ans += start + 1
        
        return ans
        

        
# @lc code=end


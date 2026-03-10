#
# @lc app=leetcode id=1470 lang=python3
#
# [1470] Shuffle the Array
#

# @lc code=start
class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        a = []
        for i in range(n):
            a.append(nums[i])
            a.append(nums[i+n])
        return a
        
# @lc code=end


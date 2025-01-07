#
# @lc app=leetcode id=1 lang=python
#
# [1] Two Sum
#

# @lc code=start
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        record = dict()
        for i, num in enumerate(nums):
            if target - num in record:
                return [record[target - num], i]
            record[num] = i
        
# @lc code=end


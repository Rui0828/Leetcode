#
# @lc app=leetcode id=35 lang=python
#
# [35] Search Insert Position
#

# @lc code=start
class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        start = 0
        end = len(nums)-1
        ans = int(len(nums)/2)
        if target > nums[-1]:
            return len(nums)
        elif target <= nums[0]:
            return 0
        while(nums[ans]<target or nums[ans-1]>=target):
            if nums[ans] < target:
                start = ans
            else:
                end = ans
            ans =  int((start+end)/2)
            
            if start == end - 1 and target > nums[ans] and target <= nums[ans+1]:
                return ans+1
            
        return ans

# @lc code=end


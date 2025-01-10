#
# @lc app=leetcode id=3194 lang=python
#
# [3194] Minimum Average of Smallest and Largest Elements
#

# @lc code=start
class Solution(object):
    def minimumAverage(self, nums):
        """
        :type nums: List[int]
        :rtype: float
        """
        rec = float(max(nums))
        while nums:
            max_num = max(nums)
            min_num = min(nums)
            
            rec = min(float((max_num + min_num))/2, rec)
            
            nums.remove(max_num)
            nums.remove(min_num)
        
        return rec
# @lc code=end

print(Solution().minimumAverage([1,9,8,3,10,5]))
print(Solution().minimumAverage([1,2,3,7,8,9]))
print(Solution().minimumAverage([7,8,3,4,15,13,4,1]))

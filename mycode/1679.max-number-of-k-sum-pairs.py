#
# @lc app=leetcode id=1679 lang=python3
#
# [1679] Max Number of K-Sum Pairs
#

# @lc code=start
class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        cnt = 0
        nums = sorted(nums)

        left, right = 0, len(nums)-1

        while left < right:
            
            v = nums[left] + nums[right]

            if v == k:
                cnt += 1
                left += 1
                right -= 1
            elif v > k:
                right -= 1
            else:
                left += 1

        return cnt
        
# @lc code=end


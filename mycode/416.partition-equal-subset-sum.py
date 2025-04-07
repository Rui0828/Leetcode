#
# @lc app=leetcode id=416 lang=python3
#
# [416] Partition Equal Subset Sum
#

# @lc code=start
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if len(nums) == 1:
            return False

        targ = sum(nums)
        if targ % 2 != 0:
            return False
        
        targ //= 2
        if targ in nums:
            return True
        elif any(x > targ for x in nums):
            return False

        nums = sorted(nums, reverse=True)

        dp = [[0] * (targ+1) for _ in nums]

        for i in range(len(nums)):
            for j in range(nums[i], targ+1):
                
                if i == 0:
                    dp[i][j] = nums[i]
                
                else:
                    dp[i][j] = max(dp[i-1][j-nums[i]] + nums[i], dp[i-1][j])

                if dp[i][j] == targ:
                    return True

        if dp[len(nums)-1][targ] == targ:
            return True
        else:
            return False

                
        
# @lc code=end


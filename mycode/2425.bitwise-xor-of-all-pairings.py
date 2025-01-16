#
# @lc app=leetcode id=2425 lang=python
#
# [2425] Bitwise XOR of All Pairings
#

# @lc code=start
class Solution(object):
    def xorAllNums(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: int
        """
        
        ans = 0
        
        if len(nums1) % 2 != 0:
            for i in nums2:
                ans ^= i
        if len(nums2) % 2 != 0:
            for i in nums1:
                ans ^= i
        
        return ans
# @lc code=end
print(Solution().xorAllNums([2,1,3], [10,2,5,0])) # 13

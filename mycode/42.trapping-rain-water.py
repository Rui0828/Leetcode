#
# @lc app=leetcode id=42 lang=python
#
# [42] Trapping Rain Water
#

# @lc code=start
class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        pre = 0
        post = len(height) - 1
        cnt = 0
        
        while pre < post:
            if height[pre] < height[post]:
                min_height = height[pre]
                pre += 1
                while pre < post and height[pre] < min_height:
                    cnt += min_height - height[pre]
                    pre += 1
            else:
                min_height = height[post]
                post -= 1
                while pre < post and height[post] < min_height:
                    cnt += min_height - height[post]
                    post -= 1
        return cnt
        
# @lc code=end

print(Solution().trap([0,1,0,2,1,0,1,3,2,1,2,1])) # 6
print(Solution().trap([4,2,0,3,2,5])) # 9
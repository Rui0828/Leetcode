#
# @lc app=leetcode id=84 lang=python3
#
# [84] Largest Rectangle in Histogram
#

# @lc code=start
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        q = []
        mx = 0
        for i in range(n):
            while q and heights[i] < heights[q[-1]]:
                h = heights[q.pop()]
                w = i-q[-1]-1 if q else i
                mx = max(mx, h*w)

            q.append(i)

        while q:
            h = heights[q.pop()]
            w = n-q[-1]-1 if q else n
            mx = max(mx, h*w)

        return mx
# @lc code=end


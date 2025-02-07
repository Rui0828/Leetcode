#
# @lc app=leetcode id=3160 lang=python3
#
# [3160] Find the Number of Distinct Colors Among the Balls
#

from typing import List
import collections

# @lc code=start
class Solution(object):
    def queryResults(self, limit, queries):
        """
        :type limit: int
        :type queries: List[List[int]]
        :rtype: List[int]
        """
        balls = collections.defaultdict(int)
        colors = collections.defaultdict(int)
        color_cnt = 0
        ans = []

        for ball, color in queries:
            if ball in balls:
                if color != balls[ball]:
                    if colors[balls[ball]] == 1:
                        del colors[balls[ball]]
                        color_cnt -= 1
                    else:
                        colors[balls[ball]] -= 1
                    
                    if color not in colors:
                        color_cnt += 1
                    colors[color] += 1
                    balls[ball] = color
            else:
                balls[ball] = color
                if color not in colors:
                    color_cnt += 1
                colors[color] += 1

            ans.append(color_cnt)
            
        return ans
        
# @lc code=end


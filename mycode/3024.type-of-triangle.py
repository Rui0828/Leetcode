#
# @lc app=leetcode id=3024 lang=python3
#
# [3024] Type of Triangle
#
from typing import List
# @lc code=start
class Solution:
    def triangleType(self, nums: List[int]) -> str:
        a = nums[0]
        b = nums[1]
        c = nums[2]

        if a==b==c:
            return "equilateral"
        elif (a==b or b==c or c==a) and a+b > c and a+c > b and b+c > a:
            return "isosceles"
        elif a+b > c and a+c > b and b+c > a:
            return "scalene"
        else:
            return "none"
        
# @lc code=end


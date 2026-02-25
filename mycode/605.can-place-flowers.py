#
# @lc app=leetcode id=605 lang=python3
#
# [605] Can Place Flowers
#

# @lc code=start
class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        
        cnt = 0
        for i in range(len(flowerbed)):
            left = i==0 or flowerbed[i-1] == 0
            right = i==len(flowerbed)-1 or flowerbed[i+1] == 0

            if flowerbed[i] == 0 and left and right:
                cnt += 1
                flowerbed[i] = 1
        
        return n <= cnt

        
# @lc code=end


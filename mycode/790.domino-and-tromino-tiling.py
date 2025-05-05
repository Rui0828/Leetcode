#
# @lc app=leetcode id=790 lang=python3
#
# [790] Domino and Tromino Tiling
#

# @lc code=start
class Solution:
    def numTilings(self, n: int) -> int:
        
        if n == 1:
            return 1
        elif n == 2 :
            return 2
        else:
            arr = [0] * (n + 1)
            arr[0] = 1
            arr[1] = 1
            arr[2] = 2
        
            bef = 1
            for i in range(3, n+1):
                arr[i] = arr[i-1] + arr[i-2] + bef * 2
                bef += arr[i-2]

            return arr[n] % (10**9+7)
        
        
# @lc code=end


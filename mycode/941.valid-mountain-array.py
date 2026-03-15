#
# @lc app=leetcode id=941 lang=python3
#
# [941] Valid Mountain Array
#

# @lc code=start
class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:

        if len(arr) < 3:
            return False
        
        inc = True
        for i in range(1, len(arr)):
            if arr[i] == arr[i-1]:
                return False
            elif arr[i] < arr[i-1]:
                inc = False

            if not inc and (i==1 or arr[i] >= arr[i-1]):
                return False

        if inc:
            return False
        
        return True
# @lc code=end


#
# @lc app=leetcode id=1354 lang=python3
#
# [1354] Construct Target Array With Multiple Sums
#
import heapq
# @lc code=start
class Solution:
    def isPossible(self, target: List[int]) -> bool:

        if len(target) == 1 and target[0] != 1:
            return False

        arr = [-x for x in target]
        heapq.heapify(arr)

        l = -heapq.heappop(arr)
        while l != 1:

            d = sum([-i for i in arr])
            if l < d + 1:
                return False

            print(l, d)
            l = l % d
            if l==0:
                l=d
            heapq.heappush(arr, -l)
            l = -heapq.heappop(arr)
        
        return True
        
# @lc code=end


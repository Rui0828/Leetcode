#
# @lc app=leetcode id=3296 lang=python3
#
# [3296] Minimum Number of Seconds to Make Mountain Height Zero
#

# @lc code=start
class Solution:
    def minNumberOfSeconds(self, mountainHeight: int, workerTimes: List[int]) -> int:
        mt = 0
        wk = [(i, i, 1) for i in workerTimes]
        heapq.heapify(wk)

        while mountainHeight != 0:
            tp = heapq.heappop(wk)
            mt = max(mt, tp[0])
            heapq.heappush(wk, (tp[0]+tp[1]*(tp[2]+1), tp[1], tp[2]+1))
            mountainHeight -= 1
        
        return mt






# @lc code=end


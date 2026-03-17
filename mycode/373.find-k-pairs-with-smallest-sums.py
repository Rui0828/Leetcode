#
# @lc app=leetcode id=373 lang=python3
#
# [373] Find K Pairs with Smallest Sums
#
from heapq import *
# @lc code=start
class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        hp = [(nums1[0]+nums2[0], 0, 0)]
        ans = []
        visited = set((0, 0))
        n1 = len(nums1)
        n2 = len(nums2)

        while hp and len(ans) < k:
            s, i, j  = heappop(hp)
            ans.append([nums1[i], nums2[j]])

            if i < n1-1 and (i+1, j) not in visited:
                heappush(hp, (nums1[i+1]+nums2[j], i+1, j))
                visited.add((i+1, j))
            if j < n2-1 and (i, j+1) not in visited:  
                heappush(hp, (nums1[i]+nums2[j+1], i, j+1))
                visited.add((i, j+1))
        
        return ans


# @lc code=end


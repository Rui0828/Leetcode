#
# @lc app=leetcode id=2359 lang=python3
#
# [2359] Find Closest Node to Given Two Nodes
#
from typing import List
# @lc code=start
class Solution:
    def closestMeetingNode(self, edges: List[int], node1: int, node2: int) -> int:
        
        tg = node1
        seen = set()
        path1_cnt = [-1] * len(edges)
        step = 0
        while tg != -1 and tg not in seen:
            seen.add(tg)
            path1_cnt[tg] = step
            step += 1
            tg = edges[tg]


        tg = node2
        seen = set()
        path2_cnt = [-1] * len(edges)
        step = 0
        while tg != -1 and tg not in seen:
            seen.add(tg)
            path2_cnt[tg] = step
            step += 1
            tg = edges[tg]
        
        ans = -1
        for i in range(len(edges)):
            if path1_cnt[i] != -1 and path2_cnt[i] != -1:
                if ans == -1:
                    ans = i
                else:
                    if max(path1_cnt[i], path2_cnt[i]) < max(path1_cnt[ans], path2_cnt[ans]):
                        ans = i
        
        return ans
        
# @lc code=end


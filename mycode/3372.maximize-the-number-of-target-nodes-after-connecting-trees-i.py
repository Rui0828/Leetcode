#
# @lc app=leetcode id=3372 lang=python3
#
# [3372] Maximize the Number of Target Nodes After Connecting Trees I
#
from typing import List
import collections
# @lc code=start
class Solution:
    def maxTargetNodes(self, edges1: List[List[int]], edges2: List[List[int]], k: int) -> List[int]:

        if k==0:
            return [1] + [1]*len(edges1)

        path1 = collections.defaultdict(list)
        path2 = collections.defaultdict(list)

        for a, b in edges1:
            path1[a].append(b)
            path1[b].append(a)
        
        for a, b in edges2:
            path2[a].append(b)
            path2[b].append(a)

        tree2max = 0
        for i in range(len(edges2)+1):
            nodecnt = 0
            arr = [(i, -1, 1)]
            while arr:
                c_node, come_node, cnt = arr.pop()
                nodecnt += 1
                for j in path2[c_node]:
                    if j != come_node and cnt < k:
                        arr.append((j, c_node, cnt+1))
            tree2max = max(tree2max, nodecnt)

        ans = []
        for i in range(len(edges1)+1):
            nodecnt = 0
            arr = [(i, -1, 0)]
            while arr:
                c_node, come_node, cnt = arr.pop()
                nodecnt += 1
                for j in path1[c_node]:
                    if j != come_node and cnt < k:
                        arr.append((j, c_node, cnt+1))
            ans.append(nodecnt+tree2max)
        
        return ans
# @lc code=end


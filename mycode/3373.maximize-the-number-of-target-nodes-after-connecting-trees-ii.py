#
# @lc app=leetcode id=3373 lang=python3
#
# [3373] Maximize the Number of Target Nodes After Connecting Trees II
#
from typing import List
import collections
# @lc code=start
class Solution:
    def maxTargetNodes(self, edges1: List[List[int]], edges2: List[List[int]]) -> List[int]:

        path1 = collections.defaultdict(list)
        path2 = collections.defaultdict(list)

        for a, b in edges1:
            path1[a].append(b)
            path1[b].append(a)
        
        for a, b in edges2:
            path2[a].append(b)
            path2[b].append(a)

        arr = [(0, -1, False)]
        t_rec = set()
        f_rec = set()

        while arr:
            c_node, come_node, tf = arr.pop()
            if tf:
                t_rec.add(c_node)
            else:
                f_rec.add(c_node)
            for j in path2[c_node]:
                if j != come_node:
                    arr.append((j, c_node, False if tf else True))
        
        tree2dmax = max(len(t_rec), len(f_rec))

        t_rec = set()
        f_rec = set()
        arr = [(0, -1, True)]
        while arr:
            c_node, come_node, tf = arr.pop()
            if tf:
                t_rec.add(c_node)
            else:
                f_rec.add(c_node)
            for j in path1[c_node]:
                if j != come_node:
                    arr.append((j, c_node, False if tf else True))
        
        ans = []
        t_cnt = len(t_rec)
        f_cnt = len(f_rec)
        for i in range(len(edges1)+1):
            if i in t_rec:
                ans.append(t_cnt + tree2dmax)
            else:
                ans.append(f_cnt + tree2dmax)
        
        return ans
# @lc code=end


#
# @lc app=leetcode id=684 lang=python3
#
# [684] Redundant Connection
#

from typing import List
import collections

# @lc code=start
class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        
        eg = collections.defaultdict(list)
        for p, q in edges:
            eg[p].append(q)
            eg[q].append(p)
        
        dq = collections.deque()
        seen = set()
        
        cycle = []
        for i in range(len(edges)):
            if i in seen:
                continue
        
            for j in eg[i]:
                dq.append((j, [i]))
                
            
            while dq:
                current, pre = dq.pop()
                
                if current in pre:
                    cycle = pre[pre.index(current):]
                    break
                
                pre.append(current)
                for j in eg[current]:
                    if j != pre[-2]:
                        dq.append((j, list(pre)))
                
                if cycle:
                    break
        
        # print(cycle)
        
        for i in range(len(edges)-1, -1, -1):
            if edges[i][0] in cycle and edges[i][1] in cycle:
                return edges[i]
# @lc code=end

# print(Solution().findRedundantConnection([[1,2],[1,3],[2,3]]))
# print(Solution().findRedundantConnection([[1,2],[2,3],[3,4],[1,4],[1,5]]))
print(Solution().findRedundantConnection([[2,7],[7,8],[3,6],[2,5],[6,8],[4,8],[2,8],[1,8],[7,10],[3,9]]))
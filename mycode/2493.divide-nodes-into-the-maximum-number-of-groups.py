#
# @lc app=leetcode id=2493 lang=python3
#
# [2493] Divide Nodes Into the Maximum Number of Groups
#

from typing import List
import collections

# @lc code=start
class Solution:
    def magnificentSets(self, n: int, edges: List[List[int]]) -> int:
        
        egs = collections.defaultdict(list)
        for a, b in edges:
            # 題目的 node 從 1 開始，所以 -1
            egs[a-1].append(b-1)
            egs[b-1].append(a-1)
        
        
        group_cnt = {} # 圖有可能不互通，用來記錄每一坨的 gruup 數量
        
        for i in range(n): # 這裡很暴力，直接從每個點開始掃，去找每一坨的群數取 max (感覺有機會優化)
            
            dq = collections.deque() # bfs
            min_node = i # 紀錄 group_cnt 時用最小的 node 當 key
            group_rec = [0] * n # 紀錄哪個 node 被分配到哪個 group (0 代表還未被看過)
            
            dq.append(i)
            group_rec[i] = 1
            
            while dq:
                
                node = dq.popleft() # bfs
                ## 這題一定要BFS，用 DFS 會出事，因為 DFS 的話原本應該放在同一群的可能會被攤開，導致誤判 return -1
                group = group_rec[node]
                if node < min_node:
                    min_node = node
                
                for j in egs[node]:
                    if group_rec[j] != 0:
                        if abs(group_rec[j] - group) != 1:
                            return -1
                    else:
                        dq.append(j)
                        group_rec[j] = group+1
            
            if min_node in group_cnt:
                group_cnt[min_node] = max(group_cnt[min_node], max(group_rec))
            else:
                group_cnt[min_node] = max(group_rec)
        
        
        return sum(group_cnt.values())

# @lc code=end

print(Solution().magnificentSets(6, [[1,2],[1,4],[1,5],[2,6],[2,3],[4,6]])) # 4
print(Solution().magnificentSets(3, [[1,2],[2,3],[3,1]])) # -1

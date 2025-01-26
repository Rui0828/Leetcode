#
# @lc app=leetcode id=2127 lang=python
#
# [2127] Maximum Employees to Be Invited to a Meeting
#

import collections

# @lc code=start
class Solution(object):
    def maximumInvitations(self, favorite):
        """
        :type favorite: List[int]
        :rtype: int
        """
        
        # 這題要找 graph 中的 cycle
        ## 當 cycle len = 2 時，還有位子讓別人指向他，因此 2 要再額外用 inv 掃瞄兩邊
        ## 且 cycle len = 2 時可以容納多組，所以可以把所有 cycle len = 2 的加起來
        
        favorite_len = len(favorite)
        
        inv = collections.defaultdict(list)
        for i in range(favorite_len):
            inv[favorite[i]].append(i)
            
        seen = set()
        max_len = 0
        all_s_len = 0 # sequence length of cycle len = 2
        
        for node in range(favorite_len):
            
            if node in seen:
                continue
            
            # 這一段的邏輯是先找 cycle
            ## 若 cycle len = 2 時，下面會再額外處理
            ## 若不是 2 我只需要考慮 cycle 的元素數量
            path = [node]
            while favorite[path[-1]] not in seen:
                seen.add(favorite[path[-1]])
                path.append(favorite[path[-1]])
                
            ## 若 favorite[path[-1]] 不在 path 中
            ### 代表 還未找到 cycle 之前，已遇到 seen 
            ### 代表在 seen 之後的 path 跟 cycle 已被看過
            #### 若 path != 2 那個 cycle 已被記錄過
            #### 若 = 2 ， 後續掃描 inv 時也會把這部分考慮進去
            ### 故可以直接 continue
            if favorite[path[-1]] not in path:
                continue
            cycle_len = len(path) - path.index(favorite[path[-1]])
            
            if cycle_len != 2:
                max_len = max(max_len, cycle_len)
            else:
                max_lr_len = [0, 0] # 記錄 len=2 左邊跟右邊兩個 node 的最長 seq
                
                # 這邊可以大膽移除，因為只需要掃過一次
                ## 也避免BFS(DFS)時無限迴圈
                inv[path[-2]].remove(path[-1])
                inv[path[-1]].remove(path[-2])
                
                for lr in range(2):
                    dq = collections.deque([(path[-1-lr], 0)]) # -1-lr = -1 and -2
                    
                    while dq:
                        i, lr_len = dq.popleft()
                        
                        if i in inv:
                            for j in inv[i]:
                                dq.append((j, lr_len + 1))
                                seen.add(j)
                        else:
                            max_lr_len[lr] = max(max_lr_len[lr], lr_len)
                
                all_s_len += 2 + sum(max_lr_len)
        
        return max(max_len, all_s_len)
# @lc code=end


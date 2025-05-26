#
# @lc app=leetcode id=1857 lang=python3
#
# [1857] Largest Color Value in a Directed Graph
#
from typing import List
import collections
# @lc code=start
class Solution:
    def largestPathValue(self, colors: str, edges: List[List[int]]) -> int:
        node_cnt = len(colors)
        path = collections.defaultdict(list)
        in_degree = [0]*node_cnt

        for u, v in edges:
            if u == v:
                return -1
            path[u].append(v)
            in_degree[v] += 1
        
        que = []
        dp = [[0] * 26 for _ in range(node_cnt)] # dp dim: node_cnt * 26
        for i in range(node_cnt):
            if in_degree[i] == 0:
                que.append(i)
                dp[i][ord(colors[i]) - ord('a')] += 1
                
        times = 0
        ans = 0
        while que:
            node = que.pop()
            times += 1

            for next_node in path[node]:
                for color in range(26):
                    add = 1 if ord(colors[next_node])-ord('a') == color else 0
                    dp[next_node][color] = max(dp[next_node][color], dp[node][color] + add)
                in_degree[next_node] -= 1


                if in_degree[next_node] == 0:
                    que.append(next_node)
                
            ans = max(ans, max(dp[node]))

        return ans if times == node_cnt else -1


# @lc code=end


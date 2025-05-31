#
# @lc app=leetcode id=909 lang=python3
#
# [909] Snakes and Ladders
#
from typing import List
import collections

# @lc code=start
class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        
        n = len(board)
        path_len = n * n
        path = [-1] * path_len
        path[0] = 0

        board_clean = []

        lr = True
        for i in range(n-1, -1, -1):
            if lr:
                lr = False
            else:
                lr = True
                board[i].reverse()
            board_clean.extend(board[i])

        que = collections.deque()
        que.append(0)

        while que:
            node = que.popleft()
            step = path[node]

            for i in range(1, 7):
                if node + i < path_len:
                    if board_clean[node + i] != -1:
                        tg = board_clean[node + i] - 1
                    else:
                        tg = node + i

                    if path[tg] == -1 or step + 1 < path[tg]:
                        path[tg] = step + 1
                        que .append(tg)

        return path[-1]
        
# @lc code=end


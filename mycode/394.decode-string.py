#
# @lc app=leetcode id=394 lang=python3
#
# [394] Decode String
#
from collections import deque
# @lc code=start
class Solution:
    def decodeString(self, s: str) -> str:
        dq = deque()
        for i in s:
            if i != ']':
                dq.append(i)
            else:
                t = ''
                while dq[-1] != '[':
                    t = dq.pop() + t
                dq.pop()

                m = ''
                while dq and dq[-1] >= '0' and dq[-1] <= '9':
                    m = dq.pop() + m
                m = int(m)
                dq.append(t * m)
        return "".join(dq)
# @lc code=end


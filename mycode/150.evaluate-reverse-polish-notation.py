#
# @lc app=leetcode id=150 lang=python3
#
# [150] Evaluate Reverse Polish Notation
#
from collections import deque
# @lc code=start
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        dq = deque()

        for i in tokens:
            if i not in '+-*/':
                dq.append(int(i))
            else:
                o2 = dq.pop()
                o1 = dq.pop()
                if i=='+':
                    dq.append(o1+o2)
                elif i=='-':
                    dq.append(o1-o2)
                elif i=='*':
                    dq.append(o1*o2)
                else:
                    dq.append(int(o1/o2))
        
        return dq[0]
        
# @lc code=end


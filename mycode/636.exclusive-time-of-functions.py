#
# @lc app=leetcode id=636 lang=python3
#
# [636] Exclusive Time of Functions
#

# @lc code=start
class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        times = [0] * n
        dq = deque()

        for log in logs:
            
            c1 = log.find(':')
            c2 = log.rfind(':')

            pid = int(log[:c1])
            start = True if log[c1+1] == 's' else False
            t = int(log[c2+1:])

            if start:
                if dq:
                    times[dq[-1]] += t - pt
                dq.append(pid)
                pt = t
            else:
                times[dq.pop()] += t - pt + 1
                pt = t+1
        return times
        
# @lc code=end


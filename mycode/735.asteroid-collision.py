#
# @lc app=leetcode id=735 lang=python3
#
# [735] Asteroid Collision
#

# @lc code=start
class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        dq = deque()
        for i in asteroids:
            if not dq or not (dq[-1]>0 and i<0):
                dq.append(i)
                continue
            
            while dq and dq[-1] > 0 and abs(dq[-1]) < abs(i):
                dq.pop()
            
            if not dq or dq[-1]<0:
                dq.append(i)
            elif dq[-1]==-i:
                dq.pop()
        
        return list(dq)

# @lc code=end


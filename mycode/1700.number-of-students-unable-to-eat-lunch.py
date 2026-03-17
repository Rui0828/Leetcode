#
# @lc app=leetcode id=1700 lang=python3
#
# [1700] Number of Students Unable to Eat Lunch
#
from collections import deque
# @lc code=start
class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        
        students = deque(students)
        sandwiches = deque(sandwiches)

        cnt = 0
        while students:
            if not len(sandwiches) % len(students) and cnt > len(sandwiches):
                break

            s = students.popleft()
            if s == sandwiches[0]:
                sandwiches.popleft()
                cnt = 0
            else:
                students.append(s)
                cnt += 1
            
             
        return len(students)
        
# @lc code=end


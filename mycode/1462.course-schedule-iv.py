#
# @lc app=leetcode id=1462 lang=python
#
# [1462] Course Schedule IV
#
import collections
# @lc code=start
class Solution(object):
    def checkIfPrerequisite(self, numCourses, prerequisites, queries):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :type queries: List[List[int]]
        :rtype: List[bool]
        """
        
        
        seen = set()
        isReachable = [[0] * numCourses for _ in range(numCourses)]
        
        
        for pre, course in prerequisites:
            
            if pre in seen or course in seen:
                pres = set([pre])
                courses = set([course])
                for j in range(numCourses):
                    if isReachable[j][pre] == 1:
                        pres.add(j)
                    if isReachable[course][j] == 1:
                        courses.add(j)
                
                for j in pres:
                    for k in courses:
                        isReachable[j][k] = 1
            else:
                isReachable[pre][course] = 1
                
            seen.add(pre)
            seen.add(course)
            
        ans = []
        for pre, course in queries:
            if isReachable[pre][course] == 1:
                ans.append(True)
            else:
                ans.append(False)
        
        return ans
# @lc code=end
# print(Solution().checkIfPrerequisite(2, [[1,0]], [[0,1],[1,0]]))
# print(Solution().checkIfPrerequisite(2, [], [[1,0],[0,1]]))
# print(Solution().checkIfPrerequisite(3, [[1,2],[1,0],[2,0]], [[1,0],[1,2]]))
print(Solution().checkIfPrerequisite(6, [[0,5],[1,2],[1,4],[2,3],[5,1]], [[0,3]]))

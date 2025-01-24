#
# @lc app=leetcode id=802 lang=python
#
# [802] Find Eventual Safe States
#

# @lc code=start
class Solution(object):
    def eventualSafeNodes(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: List[int]
        """
        len_graph = len(graph)
        inv_graph = {}
        safe =  []
        

        for i in range(len_graph):
            if graph[i]:
                for j in graph[i]:
                    if j in inv_graph:
                        inv_graph[j].append(i)
                    else:
                        inv_graph[j] = [i]
            else:
                safe.append(i)
        
        # print(inv_graph)
        
        for i in safe:
            if i in inv_graph:
                for j in inv_graph[i]:
                    if len(graph[j]) == 1:
                        safe.append(j)
                    else:
                        graph[j].remove(i)
            
        return sorted(safe)
        
# @lc code=end
print(Solution().eventualSafeNodes([[1,2],[2,3],[5],[0],[5],[],[]]))
print(Solution().eventualSafeNodes([[1,2,3,4],[1,2],[3,4],[0,4],[]]))
print(Solution().eventualSafeNodes([[1,3,4],[2,3,4],[0,3],[4],[]]))

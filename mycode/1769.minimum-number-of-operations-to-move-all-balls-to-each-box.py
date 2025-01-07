#
# @lc app=leetcode id=1769 lang=python
#
# [1769] Minimum Number of Operations to Move All Balls to Each Box
#

# @lc code=start
class Solution(object):
    def minOperations(self, boxes):
        """
        :type boxes: str
        :rtype: List[int]
        """
        len_cnt = len(boxes)
        ans = [0] * len_cnt

        ball_cnt = 0
        step_cnt = 0  
        
        for i in range(len_cnt):
            ans[i] += step_cnt
            step_cnt += ball_cnt
            if boxes[i] == '1':
                step_cnt +=1
                ball_cnt +=1
            
        
        ball_cnt = 0
        step_cnt = 0 
        
        for i in range(len_cnt-1, -1, -1):
            ans[i] += step_cnt
            step_cnt += ball_cnt
            if boxes[i] == '1':
                step_cnt +=1
                ball_cnt +=1
            
        return ans


# @lc code=end


/*
 * @lc app=leetcode id=1769 lang=c
 *
 * [1769] Minimum Number of Operations to Move All Balls to Each Box
 */

// @lc code=start
/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* minOperations(char* boxes, int* returnSize) {
    int len_cnt = strlen(boxes);
    *returnSize = len_cnt;
    
    int* ans = (int*)malloc(len_cnt * sizeof(int));
    for (int i = 0; i < len_cnt; i++) {
        ans[i] = 0;
    }
    
    int ball_cnt = 0;
    int step_cnt = 0;
    
    // Traverse from left to right
    for (int i = 0; i < len_cnt; i++) {
        ans[i] += step_cnt;
        step_cnt += ball_cnt;
        if (boxes[i] == '1') {
            step_cnt++;
            ball_cnt++;
        }
    }
    
    ball_cnt = 0;
    step_cnt = 0;
    
    // Traverse from right to left
    for (int i = len_cnt - 1; i >= 0; i--) {
        ans[i] += step_cnt;
        step_cnt += ball_cnt;
        if (boxes[i] == '1') {
            step_cnt++;
            ball_cnt++;
        }
    }
    
    return ans;
}
// @lc code=end


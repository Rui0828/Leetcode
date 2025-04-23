#
# @lc app=leetcode id=1399 lang=python3
#
# [1399] Count Largest Group
#
import collections
# @lc code=start
class Solution:
    def countLargestGroup(self, n: int) -> int:
        rec = collections.defaultdict(list)
        for i in range(1, n+1):
            dig = 0
            num = i
            while num:
                dig += num%10
                num //= 10
            
            rec[dig].append(i)
        
        rec_cnt = sorted(list(rec.values()), key=len, reverse=True)

        cnt = 1
        tg = len(rec_cnt[0])
        for i in range(1, len(rec_cnt)):
            if len(rec_cnt[i]) == tg:
                cnt += 1
            else:
                break
        
        return cnt
        
# @lc code=end


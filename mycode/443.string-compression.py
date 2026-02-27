#
# @lc app=leetcode id=443 lang=python3
#
# [443] String Compression
#

# @lc code=start
class Solution:
    def compress(self, chars: List[str]) -> int:
        
        ans = chars[0]
        cnt = 1

        for i in range(1, len(chars)):
            if chars[i] != chars[i-1]:
                if cnt != 1:
                    ans += str(cnt)
                ans += chars[i]
                cnt = 1
            else:
                cnt += 1
        
        if cnt != 1:
            ans += str(cnt)

        len_ans = len(ans)
        chars[:len_ans] = ans

        return len_ans
            
        
# @lc code=end


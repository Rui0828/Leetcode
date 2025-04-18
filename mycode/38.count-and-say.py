#
# @lc app=leetcode id=38 lang=python3
#
# [38] Count and Say
#

# @lc code=start
class Solution:
    def countAndSay(self, n: int) -> str:
        
        def rle(s):
            
            t = s[0]
            n = 1
            s_new = ""

            for i in s[1:]:
                if i == t:
                    n += 1
                else:
                    s_new += str(n) + str(t)
                    t = i
                    n = 1
            
            return s_new + str(n) + str(t)
    

        ans = "1"
        for i in range(n-1):
            ans = rle(ans)
        
        return ans
        
# @lc code=end


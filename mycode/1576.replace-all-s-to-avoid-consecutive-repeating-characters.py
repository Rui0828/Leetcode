#
# @lc app=leetcode id=1576 lang=python
#
# [1576] Replace All ?'s to Avoid Consecutive Repeating Characters
#

# @lc code=start
class Solution(object):
    def modifyString(self, s):
        """
        :type s: str
        :rtype: str
        """
        ans = ""
        
        if len(s)==1 and s == '?':
            return 'a'
        
        for i in range(len(s)):
            if s[i] != '?':
                ans += s[i]
            else:
                for j in string.ascii_lowercase[:26]:
                    if i == 0:
                        if s[i+1] != j:
                            ans += j
                            break
                        else:
                            continue
                    elif i == len(s)-1:
                        if list(ans)[i-1] != j:
                            ans += j
                            break
                        else:
                            continue
                    else:
                        if s[i+1] != j and list(ans)[i-1] != j:
                            ans += j
                            break
                        
        return ans
        
# @lc code=end


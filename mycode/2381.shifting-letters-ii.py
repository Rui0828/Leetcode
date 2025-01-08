#
# @lc app=leetcode id=2381 lang=python
#
# [2381] Shifting Letters II
#

# @lc code=start
class Solution(object):
    def shiftingLetters(self, s, shifts):
        """
        :type s: str
        :type shifts: List[List[int]]
        :rtype: str
        """
        
        sh = [0]* (len(s)+1)
        for i in shifts:
            value = -1 if i[2] == 0 else 1
            sh[i[0]] += value
            sh[i[1]+1] -= value
        
        for i in range(1, len(sh)):
            sh[i] += sh[i-1]
        
        ans = ""
        for i in range(len(s)):
            ans += chr((ord(s[i])-ord('a')+sh[i])%26 + ord('a'))
        
        return ans
# @lc code=end

print(Solution().shiftingLetters("abc", [[0,1,0],[1,2,1],[0,2,1]]))
print(Solution().shiftingLetters("dztz", [[0,0,0],[1,1,1]]))
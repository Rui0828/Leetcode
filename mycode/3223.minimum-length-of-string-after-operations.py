#
# @lc app=leetcode id=3223 lang=python
#
# [3223] Minimum Length of String After Operations
#

# @lc code=start
class Solution(object):
    def minimumLength(self, s):
        """
        :type s: str
        :rtype: int
        """
        cnt = {}
        for i in s:
            if i not in cnt:
                cnt[i] = 1
            else:
                cnt[i] += 1
        
        total = 0
        for ct in cnt.values():
            if ct % 2 == 0:
                total += 2
            else:
                total += 1
        return total
# @lc code=end

print(Solution().minimumLength("abaacbcbb")) # 5
print(Solution().minimumLength("aa")) # 2
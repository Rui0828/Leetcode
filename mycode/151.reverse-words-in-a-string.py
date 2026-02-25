#
# @lc app=leetcode id=151 lang=python3
#
# [151] Reverse Words in a String
#

# @lc code=start
class Solution:
    def reverseWords(self, s: str) -> str:
        s_list = s.split()
        s_list.reverse()
        return " ".join(s_list)
        
# @lc code=end


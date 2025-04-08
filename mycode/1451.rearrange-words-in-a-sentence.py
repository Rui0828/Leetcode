#
# @lc app=leetcode id=1451 lang=python3
#
# [1451] Rearrange Words in a Sentence
#

# @lc code=start
class Solution:
    def arrangeWords(self, text: str) -> str:
        return " ".join(sorted(text.split(), key=len)).capitalize()
        
# @lc code=end


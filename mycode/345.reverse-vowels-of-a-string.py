#
# @lc app=leetcode id=345 lang=python3
#
# [345] Reverse Vowels of a String
#

# @lc code=start
class Solution:
    def reverseVowels(self, s: str) -> str:
        s = list(s)
        left = 0
        right = len(s) - 1
        vowels = 'aeiouAEIOU'

        while left < right:

            while s[left] not in vowels and left < right:
                left += 1
            
            while s[right] not in vowels and left < right:
                right -= 1

            s[left], s[right] = s[right], s[left]

            left += 1
            right -= 1
        
        return "".join(s)
        
# @lc code=end


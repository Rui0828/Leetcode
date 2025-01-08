#
# @lc app=leetcode id=3042 lang=python
#
# [3042] Count Prefix and Suffix Pairs I
#

# @lc code=start
class Solution(object):
    def countPrefixSuffixPairs(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        ans = 0
        for i in range(len(words)):
            for j in range(i+1, len(words)):
                if words[j].startswith(words[i]) and words[j].endswith(words[i]):
                    ans += 1
        return ans
# @lc code=end

print(Solution().countPrefixSuffixPairs(["a","aba","ababa","aa"]))
print(Solution().countPrefixSuffixPairs(["pa","papa","ma","mama"]))
print(Solution().countPrefixSuffixPairs(["abab","ab"]))

#
# @lc app=leetcode id=916 lang=python
#
# [916] Word Subsets
#

# @lc code=start
class Solution(object):
    
    def word_stat(self, word):
        cnt = {}
        for i in list(word):
            if i not in cnt:
                cnt[i] = 1
            else:
                cnt[i] += 1
        return cnt
    
    def wordSubsets(self, words1, words2):
        """
        :type words1: List[str]
        :type words2: List[str]
        :rtype: List[str]
        """
        
        words2_stats = {}
        for i in words2:
            cnt = self.word_stat(i)
            for letter, l_cnt in cnt.items():
                if letter not in words2_stats:
                    words2_stats[letter] = l_cnt
                else:
                    words2_stats[letter] = max(words2_stats[letter], l_cnt)
        
        # print(words2_stats)
        
        ans = []
        for i in words1:
            chk = True
            cnt = self.word_stat(i)
            # print(cnt)
            for letter, l_cnt in words2_stats.items():
                if letter not in cnt or l_cnt > cnt[letter]:
                    # print(letter, l_cnt)
                    chk = False
                if not chk:
                    break
            if chk:
                ans.append(i)
        
        return ans
        
# @lc code=end
print(Solution().wordSubsets(["amazon","apple","facebook","google","leetcode"], ["e","o"]))
print(Solution().wordSubsets(["amazon","apple","facebook","google","leetcode"], ["l","e"]))
print(Solution().wordSubsets(["amazon","apple","facebook","google","leetcode"], ["e","oo"]))

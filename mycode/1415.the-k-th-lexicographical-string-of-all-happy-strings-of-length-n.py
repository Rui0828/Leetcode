#
# @lc app=leetcode id=1415 lang=python3
#
# [1415] The k-th Lexicographical String of All Happy Strings of Length n
#

# @lc code=start
class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        hp = ['a', 'b', 'c']

        for i in range(1, n):
            new = []
            for j in hp:
                if j[-1] != 'a':
                    new.append(j+'a')
                if j[-1] != 'b':
                    new.append(j+'b')
                if j[-1] != 'c':
                    new.append(j+'c')
            hp = new

        hp.sort()

        return hp[k-1] if len(hp)>=k else ""
# @lc code=end


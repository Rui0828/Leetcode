#
# @lc app=leetcode id=1441 lang=python3
#
# [1441] Build an Array With Stack Operations
#

# @lc code=start
class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        t = 1
        ans = []

        for i in target:
            while t < i:
                ans += ["Push", "Pop"]
                t += 1
            ans.append("Push")
            t +=1

        return ans
        
# @lc code=end


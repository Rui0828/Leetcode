#
# @lc app=leetcode id=2657 lang=python
#
# [2657] Find the Prefix Common Array of Two Arrays
#

# @lc code=start
class Solution(object):
    def findThePrefixCommonArray(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: List[int]
        """
        Arec = []
        Brec = []
        
        ans = []
        cnt = 0
        
        for i in range(len(A)):
            if A[i] == B[i]:
                cnt += 1
            else:
                if B[i] in Arec:
                    cnt += 1
                    Arec.pop(Arec.index(B[i]))
                else:
                    Brec.append(B[i])
                
                if A[i] in Brec:
                    cnt += 1
                    Brec.pop(Brec.index(A[i]))
                else:
                    Arec.append(A[i])
            ans.append(cnt)
        
        return ans
# @lc code=end

print(Solution().findThePrefixCommonArray([1,3,2,4], [3,1,2,4]))
print(Solution().findThePrefixCommonArray([2,3,1], [3,1,2]))
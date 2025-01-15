#
# @lc app=leetcode id=2429 lang=python
#
# [2429] Minimize XOR
#

# @lc code=start
class Solution(object):
    def minimizeXor(self, num1, num2):
        """
        :type num1: int
        :type num2: int
        :rtype: int
        """
        bin1 = "{0:b}".format(num1).zfill(max(len("{0:b}".format(num1)), len("{0:b}".format(num2))))
        cnt1 = bin1.count("1")
        cnt2 = "{0:b}".format(num2).count("1") - cnt1
        
        # print(bin1)
        
        if cnt2 < 0:
            for i in range(len(bin1)-1, -1, -1):
                if bin1[i] == "1":
                    bin1 = bin1[:i] + "0" + bin1[i+1:]
                    # print(bin1)
                    cnt2 += 1
                if cnt2 == 0:
                    break
        elif cnt2 > 0:
            for i in range(len(bin1)-1, -1, -1):
                if bin1[i] == "0":
                    bin1 = bin1[:i] + "1" + bin1[i+1:]
                    # print(bin1)
                    cnt2 -= 1
                if cnt2 == 0:
                    break
        
        return int(bin1, 2)
        
        
        
# @lc code=end

print("-"*100)
print(Solution().minimizeXor(3, 5)) # 3
print("-"*100)
print(Solution().minimizeXor(1, 12)) # 3
print("-"*100)
#
# @lc app=leetcode id=67 lang=python
#
# [67] Add Binary
#

# @lc code=start
class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        ans = ""
        carry = False
        while a or b:
            if not a:
                ans = str(int((b[-1] == '1') ^ carry)) + ans
                carry = (b[-1] == '1') & carry
                b = b[:-1]
            elif not b:
                ans = str(int((a[-1] == '1') ^ carry)) + ans
                carry = (a[-1] == '1') & carry
                a = a[:-1]
            else:
                a_chk = a[-1] == '1'
                b_chk = b[-1] == '1'
                ans = str(int((a_chk ^ b_chk) ^ carry)) + ans
                carry = (a_chk and b_chk) or (a_chk and carry) or (b_chk and carry)
                a = a[:-1]
                b = b[:-1]
        
        if carry:
            ans = '1' + ans
        return ans
# @lc code=end

# print(Solution().addBinary("11", "1"))
print(Solution().addBinary("1010", "1011"))


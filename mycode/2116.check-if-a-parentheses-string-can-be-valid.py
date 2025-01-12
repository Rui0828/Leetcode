#
# @lc app=leetcode id=2116 lang=python
#
# [2116] Check if a Parentheses String Can Be Valid
#

# @lc code=start
class Solution(object):
    def canBeValid(self, s, locked):
        """
        :type s: str
        :type locked: str
        :rtype: bool
        """
        if len(s) % 2 != 0:
            return False
        
        any_stack = []
        left_stack = []
        for i in range(len(s)):
            if locked[i] == '0':
                any_stack.append(i)
            else:
                if s[i] == '(':
                    left_stack.append(i)
                else:
                    if not left_stack:
                        if not any_stack:
                            return False
                        else:
                            any_stack.pop()
                    else:
                        left_stack.pop()
        
        
        for i in range(len(left_stack)-1, -1, -1):
            if any_stack and any_stack[-1] > left_stack[i]:
                any_stack.pop()
            else:
                return False
            
        return True
# @lc code=end
# print(Solution().canBeValid("))()))", "010100"))
# print(Solution().canBeValid("()()", "0000"))
# print(Solution().canBeValid(")", "0"))
print(Solution().canBeValid(
    "())(()(()(())()())(())((())(()())((())))))(((((((())(()))))(", "100011110110011011010111100111011101111110000101001101001111"))
# ""()))(()(()()()()(((())())((()((())"\n"1100000000000010000100001000001101""
/*
 * @lc app=leetcode id=9 lang=cpp
 *
 * [9] Palindrome Number
 */

// @lc code=start
class Solution {
public:
    bool isPalindrome(int x) {
        
        string str = to_string(x);
        int str_len = str.length();
        bool err = true;

        for(int i=0; i<str_len/2; i++) {
            if(str[i] != str[str_len-i-1])
            {
                err = false;
                break;
            }
        }
        return err;
    }
};
// @lc code=end


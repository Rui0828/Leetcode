#
# @lc app=leetcode id=2999 lang=python3
#
# [2999] Count the Number of Powerful Integers
#

# @lc code=start
class Solution:
    def numberOfPowerfulInt(self, start: int, finish: int, limit: int, s: str) -> int:
        
        str_start = str(start)
        if start <= int(s):
            st = "0"
        elif len(str_start) == len(s):
            st = "1"
        elif int(str_start[-len(s):]) <= int(s):
            st = str_start[:-len(s)]
        else:
            st = str(int(str_start[:-len(s)])+1)

        str_fin = str(finish)
        if int(s) > finish:
            return 0
        elif int(s) == finish:
            return 1
        elif int(str_fin[-len(s):]) >= int(s):
            end = str_fin[:-len(s)]
        else:
            end = str(int(str_fin[:-len(s)])-1)

        #################

        digs = max(len(st), len(end))
        end = end.zfill(digs)
        st = st.zfill(digs)

        if st[:-1] == end[:-1]:
            t = min(int(end[-1]), limit)
            if t < int(st[-1]):
                return 0
            else:
                return t-int(st[-1])+1
        else:
            
            cnt = 0
            al = 1
            for i in range(digs-1, 0, -1):

                if not any(int(digit) > limit for digit in end[:i]):
                    if int(end[i]) <= limit:
                        if al == 1:
                            cnt += (int(end[i]) + 1) * al
                        else:
                            cnt += int(end[i]) * al
                    else:
                        cnt += (limit + 1) * al
                

                if not any(int(digit) > limit for digit in st[:i+1]):
                    if al == 1:
                        cnt += (limit - int(st[i]) + 1) * al
                    else:
                        cnt += (limit - int(st[i])) * al

                al *= (limit+1)
            

            if int(st[0]) <= limit:
                if int(end[0]) > limit:
                    cnt += (limit-int(st[0]))*al
                else:
                    cnt += (int(end[0])-int(st[0])-1)*al

        return cnt
            
# @lc code=end


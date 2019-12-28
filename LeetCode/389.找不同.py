#
# @lc app=leetcode.cn id=389 lang=python3
#
# [389] 找不同
#

# @lc code=start
class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        self.s=s
        self.t=t
        s=list(s)
        t=list(t)
        nums=[]
        for i in range(len(s)):
            First=s[i]
            for j in range(len(t)):
                Second=t[j]
                if(First==Second):
                    Second=-1
                    t[j]=Second
                    break
        for i in range(len(t)):
            if(t[i]!=-1):
                nums.append(t[i])
                str_1="".join(nums)
        return str_1
# @lc code=end


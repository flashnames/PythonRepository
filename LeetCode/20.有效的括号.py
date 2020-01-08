#
# @lc app=leetcode.cn id=20 lang=python3
#
# [20] 有效的括号
#

# @lc code=start
class Solution:
    def isValid(self, s: str):
        List=list(s)
        if len(List)==1:
            return False
        for i in range(len(List)):
            if List[i]=="[":
                if List[len(List)-i-1]!="]":
                    if List[i+1]=="]":
                        pass
                    else:
                        return False
            if List[i]=="(":
                if List[len(List)-i-1]!=")":
                    if List[i+1]==")":
                        pass
                    else:
                        return False
            if List[i]=="{":
                if List[len(List)-i-1]!="}":
                    if List[i+1]=="}":
                        pass
                    else:
                        return False
        return True

if __name__=="__main__":
    print(Solution().isValid("){"))
# @lc code=end


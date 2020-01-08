#
# @lc app=leetcode.cn id=520 lang=python3
#
# [520] 检测大写字母
#

# @lc code=start
class Solution:
    def detectCapitalUse(self, word):
        Count=0
        List=list(word)
        count=0
        for Word in List:
            if Word>="A" and Word<="Z":
                Count+=1
        if Count!=len(List):
            if Count==1:
                if List[0]>="A" and List[0]<="Z":
                    return True
                else:
                    return False
            elif Count==0:
                for Word in List:
                    if Word>="a" and Word<="z":
                        count+=1
                if count==len(List):
                    return True
                else:
                    return False 
        else:
            return True
if __name__=="__main__":
    print(Solution().detectCapitalUse("USA"))
# @lc code=end


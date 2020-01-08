#
# @lc app=leetcode.cn id=58 lang=python3
#
# [58] 最后一个单词的长度
#

# @lc code=start
class Solution:
    def lengthOfLastWord(self, s: str):
        s=s.strip()
        s=s.split(" ")
        List=s[-1]
        List=list(List)
        return len(List)

if __name__=="__main__":
    print(Solution().lengthOfLastWord("a "))
# @lc code=end


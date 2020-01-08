#
# @lc app=leetcode.cn id=1108 lang=python3
#
# [1108] IP 地址无效化
#

# @lc code=start
class Solution:
    def defangIPaddr(self, address: str) -> str:
        List=list(address)
        for i in range(len(List)):
            ipadd=List[i]
            if ipadd==".":
                ipadd="[.]"
                List[i]=ipadd
        List="".join(List)
        return List
# @lc code=end


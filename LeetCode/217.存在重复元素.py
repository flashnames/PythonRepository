#
# @lc app=leetcode.cn id=217 lang=python3
#
# [217] 存在重复元素
#

# @lc code=start
class Solution:
    def containsDuplicate(self, nums):
        List=set(nums)
        if len(List)!=len(nums):
            return True
        else:
            return False

if __name__=="__main__":
    print(Solution().containsDuplicate([1,2,3,1]))
# @lc code=end

